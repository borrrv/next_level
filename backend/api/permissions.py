from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_active
                or request.method in SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_staff
                or request.user.is_superuser
                or request.method in SAFE_METHODS)
