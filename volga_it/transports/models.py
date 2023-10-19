from django.db import models


class Transports(models.Model):
    TRANSPORT_TYPES = [
        ('C', 'Car'),
        ('B', 'Bike'),
        ('S', 'Scooter')
    ]
    canBeRented = models.BooleanField(default=False, verbose_name='Можно ли арендовать транспорт?')
    transportType = models.CharField(max_length=10, choices=TRANSPORT_TYPES, verbose_name='Тип транспорта')
    model = models.CharField(max_length=100, verbose_name='Модель транспорта')
    color = models.CharField(max_length=50, verbose_name='Цвет транспорта')
    identifier = models.CharField(max_length=20, verbose_name='Номерной знак')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    latitude = models.DecimalField(default=0, max_digits=5, decimal_places=2,
                                   verbose_name='Географическая широта местонахождения транспорта')
    longitude = models.DecimalField(default=0, max_digits=5, decimal_places=2,
                                    verbose_name='Географическая долгота местонахождения транспорта')
    minutePrice = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True, null=True,
                                      verbose_name='Цена аренды за минуту')
    dayPrice = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True, null=True,
                                   verbose_name='Цена аренды за сутки')

    def __str__(self):
        return f'{self.model} - {self.color}'
