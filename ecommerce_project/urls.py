from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
]
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Welcome to Cargo E-commerce!</h1>')
urlpatterns += [path('', home)]
