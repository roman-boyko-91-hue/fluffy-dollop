from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, obj, view):
        return obj.owner == request.user
