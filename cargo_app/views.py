from django.shortcuts import render

def home(request):
    apps = ['Accounts', 'Cart', 'Catalog', 'Dashboard', 'Orders', 'Payments', 'Shipping']
    return render(request, 'home/landing.html', {'apps': apps})
