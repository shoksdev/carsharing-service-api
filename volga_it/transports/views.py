from rest_framework import viewsets
from rest_framework import generics

from .models import Transports
from .paginations import TransportPagination
from .permissions import TransportListPermission, TransportObjectPermission
from .serializers import TransportsSerializer


# class TransportViewSet(viewsets.ModelViewSet):
#     queryset = Transports.objects.all()
#     serializer_class = TransportsSerializer
#     permission_classes = [TransportPermission, ]
#     pagination_class = TransportPagination


class TransportListCreateView(generics.ListCreateAPIView):
    queryset = Transports.objects.all()
    serializer_class = TransportsSerializer
    permission_classes = [TransportListPermission, ]
    pagination_class = TransportPagination


class TransportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transports.objects.all()
    serializer_class = TransportsSerializer
    permission_classes = [TransportObjectPermission, ]
