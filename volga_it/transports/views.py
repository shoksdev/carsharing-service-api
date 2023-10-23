from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .filters import TransportAdminFilter
from .models import Transports
from .paginations import TransportPagination
from .permissions import TransportListPermission, TransportObjectPermission
from .serializers import TransportsSerializer, TransportsAdminSerializer


class TransportCreateView(generics.CreateAPIView):
    queryset = Transports.objects.all()
    serializer_class = TransportsSerializer
    permission_classes = [TransportListPermission, ]
    pagination_class = TransportPagination


class TransportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transports.objects.all()
    serializer_class = TransportsSerializer
    permission_classes = [TransportObjectPermission, ]


class TransportAdminViewSet(viewsets.ModelViewSet):
    queryset = Transports.objects.all()
    serializer_class = TransportsAdminSerializer
    pagination_class = TransportPagination
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TransportAdminFilter
