﻿from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_home, name='catalog_home'),
]
