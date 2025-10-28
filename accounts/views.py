from django.http import JsonResponse
import requests
from django.conf import settings

def test_middleware(request):
    try:
        response = requests.get(f"{settings.MIDDLEWARE_API_URL}")
        data = response.json()
        return JsonResponse({
            "middleware": data,
            "status": "? Connected"
        })
    except Exception as e:
        return JsonResponse({
            "error": str(e),
            "django_status": "? Django could not reach middleware"
        })
