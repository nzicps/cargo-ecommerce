# ===============================
# Corrected Django views.py
# All POST views are csrf_exempt
# ===============================

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# ===============================
# POST Views
# ===============================

@csrf_exempt
def start_payment(request):
    if request.method == "POST":
        # TODO: Add your POST logic here
        return JsonResponse({"status": "payment started"})
    return JsonResponse({"error": "Only POST allowed"}, status=405)

@csrf_exempt
def process_payment(request):
    if request.method == "POST":
        # TODO: Add your POST logic here
        return JsonResponse({"status": "payment processed"})
    return JsonResponse({"error": "Only POST allowed"}, status=405)

# ===============================
# GET Views (No csrf_exempt needed)
# ===============================

def payment_status(request):
    if request.method == "GET":
        # TODO: Add your GET logic here
        return JsonResponse({"status": "pending"})
    return JsonResponse({"error": "Only GET allowed"}, status=405)

def list_payments(request):
    if request.method == "GET":
        # TODO: Add your GET logic here
        return JsonResponse({"payments": []})
    return JsonResponse({"error": "Only GET allowed"}, status=405)
