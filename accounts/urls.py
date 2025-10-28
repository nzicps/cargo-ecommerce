from django.urls import path
from . import views

urlpatterns = [
    path('test-middleware/', views.test_middleware, name='test_middleware'),
]
