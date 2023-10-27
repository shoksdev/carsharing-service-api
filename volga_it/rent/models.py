from django.db import models

from users.models import CustomUser

from transports.models import Transports


class Rent(models.Model):
    PRICE_TYPES = [
        ('M', 'Minutes'),
        ('D', 'Days'),
    ]
    transport = models.ForeignKey(Transports, on_delete=models.CASCADE, verbose_name='Транспорт')
    time_start = models.DateTimeField(auto_now_add=True, verbose_name='Время начала аренды')
    time_end = models.DateTimeField(null=True, blank=True, verbose_name='Время конца аренды')
    price_of_unit = models.FloatField(default=0, verbose_name='Цена единицы времени аренды')
    price_type = models.CharField(max_length=10, choices=PRICE_TYPES, verbose_name='Тип аренды')
    final_price = models.FloatField(null=True, blank=True, verbose_name='Финальная цена аренды')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Арендатор')

    def __str__(self):
        return f'{self.transport}:{self.time_start}-{self.time_end}'
