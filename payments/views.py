import json, requests
from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from django.apps import apps
from .models import Payment
from .utils import generate_akurateco_hash

AKURATECO_MERCHANT_KEY = getattr(settings, 'AKURATECO_MERCHANT_KEY', 'YOUR_MERCHANT_KEY')
AKURATECO_SECRET_KEY = getattr(settings, 'AKURATECO_SECRET_KEY', 'YOUR_SECRET_KEY')
AKURATECO_API_BASE_URL = getattr(settings, 'AKURATECO_API_BASE_URL', 'https://sandbox.akurateco.com/api/v1/session')

def get_order_model():
    for app_config in apps.get_app_configs():
        try:
            return app_config.get_model('Order')
        except LookupError:
            continue
    return None

def detect_customer_field(Order):
    for f in Order._meta.fields:
        if f.is_relation and f.related_model._meta.object_name == 'User':
            return f.name
    return None

def start_payment(request, order_id, currency='USD'):
    Order = get_order_model()
    if not Order:
        return render(request, 'payments/cancel.html', {'error': 'Order model not found'})
    customer_field = detect_customer_field(Order)
    order = get_object_or_404(Order, id=order_id)
    customer = getattr(order, customer_field) if customer_field else None

    payload = {
        'merchant_key': AKURATECO_MERCHANT_KEY,
        'operation': 'purchase',
        'order': {'number': str(order.id), 'amount': str(order.total), 'currency': currency, 'description': f'Payment for Order {order.id}'},
        'customer': {'email': getattr(customer,'email','') if customer else '', 'name': getattr(customer,'username','') if customer else ''},
        'success_url': request.build_absolute_uri('/payments/success/'),
        'cancel_url': request.build_absolute_uri('/payments/cancel/'),
    }

    payload['hash'] = generate_akurateco_hash(AKURATECO_MERCHANT_KEY, order.id, order.total, AKURATECO_SECRET_KEY)

    try:
        resp = requests.post(AKURATECO_API_BASE_URL, json=payload, timeout=15).json()
        if 'redirect_url' in resp:
            Payment.objects.create(order_id=order.id, amount=order.total, currency=currency, status='initiated')
            return redirect(resp['redirect_url'])
        else:
            return render(request, 'payments/cancel.html', {'error': resp})
    except Exception as e:
        return render(request, 'payments/cancel.html', {'error': str(e)})

@csrf_exempt
def akurateco_webhook(request):
    try:
        data = json.loads(request.body.decode())
        order_id = data.get('order', {}).get('number')
        status = data.get('status')
        p = Payment.objects.filter(order_id=order_id).first()
        if p: p.status = status; p.transaction_id = data.get('transaction_id'); p.save()
        return JsonResponse({'ok': True})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': str(e)})

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_cancel(request):
    return render(request, 'payments/cancel.html')
