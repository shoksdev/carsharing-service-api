from rest_framework import permissions


class TransportPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated
        elif view.action == 'destroy' or view.action == 'update':
            return obj.owner == request.user
