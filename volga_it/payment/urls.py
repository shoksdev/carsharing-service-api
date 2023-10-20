from django.contrib import admin
from django.urls import path, include

from .views import payment_controller

urlpatterns = [
    path('payment/hesoyam/<int:pk>/', payment_controller, name='hesoyam'),
]
