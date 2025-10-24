from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('start/<int:order_id>/', views.start_payment, name='start_payment'),
    path('webhook/', views.akurateco_webhook, name='akurateco_webhook'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]
