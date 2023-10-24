from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from djoser.views import UserViewSet

from users.models import CustomUser

from .filters import AccountAdminFilter
from .serializers import AccountSerializer
from transports.paginations import CustomPagination


class RetrieveAccountAPIView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user


class UpdateAccountAPIView(generics.UpdateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user


class RegisterAccountViewSet(UserViewSet):
    queryset = CustomUser.objects.all()


class AccountAdminViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AccountAdminFilter
