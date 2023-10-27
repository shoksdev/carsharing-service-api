from rest_framework import permissions


class RentObjectPermission(permissions.BasePermission):
    """Кастомные разрешения для аренды, проверяет является ли пользователь хозяином машины или арендатором"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.transport.owner == request.user or obj.user == request.user
