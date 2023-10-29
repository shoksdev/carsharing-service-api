from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    balance = models.FloatField(default=0, null=True, blank=True, verbose_name='Баланс пользователя')
    # Используем аргумент "default", чтобы работала функция payment_controller

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
