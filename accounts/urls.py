from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accounts-index'),
]
from . import views
urlpatterns += [
    path("api/test-middleware/", views.test_middleware),
]
