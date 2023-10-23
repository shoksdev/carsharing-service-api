from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from users.models import CustomUser

from .filters import AccountAdminFilter
from .serializers import AccountSerializer
from transports.paginations import CustomPagination


class AccountAPIView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer

    def get_object(self):
        return self.request.user


class AccountAdminViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AccountAdminFilter
