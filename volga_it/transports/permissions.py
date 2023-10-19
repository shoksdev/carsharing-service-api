from rest_framework import permissions


class TransportListPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif view.action == 'create':
            return request.user.is_authenticated


class TransportObjectPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif view.action == 'destroy' or view.action == 'update':
            return obj.owner == request.user
