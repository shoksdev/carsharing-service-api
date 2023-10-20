from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    balance = models.FloatField(default=0, verbose_name='Баланс пользователя')
