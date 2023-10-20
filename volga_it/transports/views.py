from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .models import Transports
from .paginations import TransportPagination
from .permissions import TransportListPermission, TransportObjectPermission
from .serializers import TransportsSerializer, TransportsAdminSerializer


class TransportListCreateView(generics.ListCreateAPIView):
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
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['transportType', ]
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Purchase.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(purchaser__username=username)
    #     return queryset
