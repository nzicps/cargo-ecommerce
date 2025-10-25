from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('start/', views.start_payment, name='start_payment'),
    path('success/', lambda request: render(request, 'payments/success.html'), name='payment_success'),
    path('cancel/', lambda request: render(request, 'payments/cancel.html'), name='payment_cancel'),
]
