from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from djoser.views import UserViewSet

from .filters import AccountAdminFilter
from .serializers import AccountSerializer
from users.models import CustomUser
from transports.paginations import CustomPagination


class RetrieveAccountAPIView(generics.RetrieveAPIView):
    """Выводит информацию о текущем пользователе"""
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user


class UpdateAccountAPIView(generics.UpdateAPIView):
    """Позволяет изменить данные о текущем пользователе"""
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user


class RegisterAccountViewSet(UserViewSet):
    """Создаёт аккаунт, был переопределен для изменения пути"""
    queryset = CustomUser.objects.all()


class AccountAdminViewSet(viewsets.ModelViewSet):
    """Вьюсет, отвечающий за взаимодействие с моделью Кастомного Пользователя (CRUD), доступно только администратору"""
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AccountAdminFilter
