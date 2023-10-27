from django.urls import path

from .views import payment_controller

urlpatterns = [
    path('hesoyam/<int:pk>/', payment_controller, name='hesoyam'),
]
