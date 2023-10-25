import json

from django.db.models import Q
from geopy.distance import geodesic
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import RentSerializer
from transports.models import Transports

from transports.serializers import TransportsSerializer


# Возможно использовать Яндекс.Геокодер

class RentListAPIView(ListAPIView):
    serializer_class = TransportsSerializer

    def get_queryset(self):
        body = json.loads(self.request.body)

        rent_lat = body.get('lat')
        rent_long = body.get('long')
        rad = body.get('radius')
        rent_transport_type = body.get('transport_type')
        transports = Transports.objects.all().values_list('latitude', 'longitude')

        suitable_transports_latitudes = []
        suitable_transports_longitudes = []

        circle_center = (rent_lat, rent_long)
        for latitude, longitude in transports:
            transport_point = (latitude, longitude)
            if geodesic(circle_center, transport_point).kilometers <= rad:
                suitable_transports_latitudes.append(latitude)
                suitable_transports_longitudes.append(longitude)
        if rent_transport_type == 'All':
            return Transports.objects.filter(
                Q(latitude__in=suitable_transports_latitudes) & Q(longitude__in=suitable_transports_longitudes)
            )
        else:
            return Transports.objects.filter(
                Q(latitude__in=suitable_transports_latitudes) & Q(longitude__in=suitable_transports_longitudes)
                & Q(transport_type=rent_transport_type)
            )
