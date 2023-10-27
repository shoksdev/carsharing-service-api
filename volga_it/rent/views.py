import json
from datetime import datetime
from django.db.models import Q
from django.http import JsonResponse
from geopy.distance import geodesic
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Rent
from .permissions import RentObjectPermission
from .serializers import RentSerializer
from transports.models import Transports

from transports.serializers import TransportsSerializer

'''Rent User'''


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


class RentMyHistoryAPIView(ListAPIView):
    serializer_class = RentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Rent.objects.filter(user=self.request.user)


class RentInfoAPIView(RetrieveAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [RentObjectPermission, ]


class RentTransportHistoryAPIView(ListAPIView):
    serializer_class = RentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self, *args, **kwargs):
        return Rent.objects.filter(transport_id=self.kwargs['pk'], transport__owner=self.request.user)


@api_view(['POST'])
def new_rent(request, pk):
    transport = Transports.objects.get(id=pk)
    if request.user.is_authenticated and transport.owner != request.user:
        body = json.loads(request.body)
        rent_type = body.get('rent_type')

        rent_data = {
            "transport_id": pk,
            "time_start": datetime.now(),
            "price_type": rent_type,
            "user": request.user
        }

        Rent.objects.create(**rent_data)

        message = {
            "message": "Аренды машины начата!"
        }
        return JsonResponse(message, status=201)
    else:
        message = {
            "message": "Вы не можете арендовать собственную машину!"
        }
        return JsonResponse(message, status=403)


class RentCreateAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer


@api_view(['POST'])
def rent_end(request, pk):
    rent = Rent.objects.get(id=pk)
    if request.user == rent.user:
        body = json.loads(request.body)
        lat = body.get('lat')
        long = body.get('long')

        transport = Transports.objects.get(id=rent.transport_id)

        rent.time_end = datetime.now()
        transport.latitude = lat
        transport.longitude = long
        rent.save()
        transport.save()

        message = {
            "message": "Аренды машины завершена!"
        }
        return JsonResponse(message, status=200)


'''Rent Admin'''


class AdminRentUserHistoryAPIView(ListAPIView):
    serializer_class = RentSerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self, *args, **kwargs):
        return Rent.objects.filter(user_id=self.kwargs['pk'])


class AdminRentTransportHistoryAPIView(ListAPIView):
    serializer_class = RentSerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self, *args, **kwargs):
        return Rent.objects.filter(transport_id=self.kwargs['pk'])


@api_view(['POST'])
def rent_end_admin(request, pk):
    rent = Rent.objects.get(id=pk)
    if request.user.is_staff or request.user == rent.user:
        body = json.loads(request.body)
        lat = body.get('lat')
        long = body.get('long')

        transport = Transports.objects.get(id=rent.transport_id)

        rent.time_end = datetime.now()
        transport.latitude = lat
        transport.longitude = long
        rent.save()
        transport.save()

        message = {
            "message": "Аренды машины завершена!"
        }
        return JsonResponse(message, status=200)


class AdminRentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [IsAdminUser, ]
