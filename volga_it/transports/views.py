from django.shortcuts import render
from rest_framework import viewsets

from .models import Transports
from .paginations import TransportPagination
from .permissions import TransportPermission
from .serializers import TransportsSerializer


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transports.objects.all()
    serializer_class = TransportsSerializer
    permission_classes = [TransportPermission]
    pagination_class = TransportPagination
