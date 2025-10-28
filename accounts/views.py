from django.shortcuts import render
def index(request):
    return render(request, 'accounts/index.html')
import os, requests
from django.http import JsonResponse

def test_middleware(request):
    middleware_url = os.getenv("MIDDLEWARE_URL", "")
    try:
        r = requests.get(f"{middleware_url}/", timeout=10)
        return JsonResponse({
            "middleware_status": r.json(),
            "django_status": "✅ Django connected to middleware successfully!"
        })
    except Exception as e:
        return JsonResponse({
            "error": str(e),
            "django_status": "❌ Django could not reach middleware"
        }, status=500)
