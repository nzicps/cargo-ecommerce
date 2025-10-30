from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Cargo E-commerce</h1><p>Your Django app is live on Render </p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
