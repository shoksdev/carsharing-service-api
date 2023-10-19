from django.shortcuts import render
from rest_framework import viewsets

from .models import Transports

from .serializers import TransportsSerializer


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transports.objects.all()
    serializer_class = TransportsSerializer
