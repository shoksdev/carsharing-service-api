from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .filters import TransportAdminFilter
from .models import Transports
from .paginations import CustomPagination
from .permissions import TransportListPermission, TransportObjectPermission
from .serializers import TransportsSerializer, TransportsAdminSerializer


class TransportCreateView(generics.CreateAPIView):
    """Создаёт объект модели транспорта, просмотр доступен любому пользователю, создать только аутентифицированный"""
    queryset = Transports.objects.all()
    serializer_class = TransportsSerializer
    permission_classes = [TransportListPermission, ]
    pagination_class = CustomPagination


class TransportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Выводит информацию о текущем объекте модели Транспорт, также позволяет изменять и удалять данные только
    владельцу этого транспорта"""
    queryset = Transports.objects.all()
    serializer_class = TransportsSerializer
    permission_classes = [TransportObjectPermission, ]


class TransportAdminViewSet(viewsets.ModelViewSet):
    """Вьюсет, отвечающий за взаимодействие с моделью Транспорта (CRUD), доступно только администратору"""
    queryset = Transports.objects.all()
    serializer_class = TransportsAdminSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TransportAdminFilter
