from rest_framework.permissions import BasePermission


class CheckObjectLevelPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False


class IsSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False
