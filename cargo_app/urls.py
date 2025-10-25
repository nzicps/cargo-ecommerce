from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('payments/', include('payments.urls')),
    path('admin/', admin.site.urls),
    path('', views.products_view, name='products'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-success/', views.order_success_view, name='order_success'),
    path('cargo/', views.cargo_view, name='cargo'),
]

