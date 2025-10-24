import hashlib

def generate_akurateco_hash(merchant_key, order_number, amount, secret_key):
    sign_string = f'{merchant_key}{order_number}{amount}{secret_key}'
    return hashlib.sha256(sign_string.encode()).hexdigest()
