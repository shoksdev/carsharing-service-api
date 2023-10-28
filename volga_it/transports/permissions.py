from rest_framework import permissions


class TransportListPermission(permissions.BasePermission):
    """Кастомные разрешения для взаимодействия с транспортом, проверяет является ли пользователь авторизованным,
    если да, даёт право на создание объекта модели, иначе только на просмотр"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated


class TransportObjectPermission(permissions.BasePermission):
    """Кастомные разрешения для взаимодействия с транспортом, проверяет является ли пользователь хозяином машины,
    если да, то даёт ему право на удаление/изменение объекта, иначе только на просмотр"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'DELETE' or request.method == 'PUT':
            return obj.owner == request.user
