import requests
import uuid

# 🌍 Akurateco Sandbox API (Test Environment)
AKURATECO_API_URL = "https://sandbox.akurateco.com/api/v1/payment"
MERCHANT_ID = "demo_merchant"
API_SECRET = "demo_secret_key"
RETURN_URL = "http://127.0.0.1:8000/payments/success/"
CANCEL_URL = "http://127.0.0.1:8000/payments/cancel/"

def create_payment(order_id, amount, customer_email):
    transaction_id = str(uuid.uuid4())
    payload = {
        "merchant": MERCHANT_ID,
        "order_id": order_id,
        "amount": str(amount),
        "currency": "USD",
        "description": "Cargo E-commerce Order",
        "customer_email": customer_email,
        "transaction_id": transaction_id,
        "success_url": RETURN_URL,
        "fail_url": CANCEL_URL,
    }
    headers = {
        "Authorization": f"Bearer {API_SECRET}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.post(AKURATECO_API_URL, json=payload, headers=headers)
        data = response.json()
        if response.status_code == 200 and "redirect_url" in data:
            return data["redirect_url"]
        else:
            print("⚠️ Payment gateway response:", data)
            return None
    except Exception as e:
        print("❌ Error creating payment:", e)
        return None
