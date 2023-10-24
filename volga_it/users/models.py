from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    balance = models.FloatField(null=True, blank=True, verbose_name='Баланс пользователя')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
