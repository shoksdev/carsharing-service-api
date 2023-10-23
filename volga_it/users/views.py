from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from users.models import CustomUser

from .filters import AccountAdminFilter
from .serializers import AdminAccountSerializer
from transports.paginations import CustomPagination


class AccountAdminViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AdminAccountSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AccountAdminFilter
