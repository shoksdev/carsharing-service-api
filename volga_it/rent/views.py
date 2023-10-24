import math

from rest_framework import viewsets

from .serializers import RentSerializer
from ..transports.models import Transports


# Возможно использовать Яндекс.Геокодер

class RentViewSet(viewsets.ModelViewSet):
    serializer_class = RentSerializer

    def get_queryset(self):
        lat = self.kwargs['lat']
        long = self.kwargs['long']
        rad = self.kwargs['radius']

        hypotenuse = math.sqrt(lat ** 2 + long ** 2)

        return Transports.objects.filter(
            Q(lat__gte=lat - rad, lat__lte=lat + rad) &
            Q(long__gte=long - rad, long__lte=long + rad) &
            Q(radius__lte=hypotenuse)
        )
