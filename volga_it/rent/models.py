from django.db import models


class Rent(models.Model):
    TRANSPORT_TYPES = [
        ('A', 'All'),
        ('C', 'Car'),
        ('B', 'Bike'),
        ('S', 'Scooter')
    ]
    lat = models.DecimalField(default=0, max_digits=5, decimal_places=2,
                              verbose_name='Географическая широта местонахождения транспорта')
    long = models.DecimalField(default=0, max_digits=5, decimal_places=2,
                               verbose_name='Географическая долгота местонахождения транспорта')
    radius = models.DecimalField(default=0, max_digits=5, decimal_places=2,
                                 verbose_name='Радиус круга поиска транспорта')
    type = models.CharField(max_length=10, choices=TRANSPORT_TYPES, verbose_name='Тип транспорта')

    def __str__(self):
        return f'{self.lat}{self.long}'
