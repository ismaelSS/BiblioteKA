from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAccountOwnerOrAdminOnlyGetOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        if request.method == "GET":
            return (
                request.user.is_authenticated
                and obj == request.user
                or request.user.is_authenticated
                and request.user.is_admin
            )
        else:
            return request.user.is_authenticated and obj == request.user


class IsAdminOnlyGET(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method == "GET":
            return request.user.is_authenticated and request.user.is_admin
        else:
            return True


class IsAdminOrOnlyGET(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method != "GET":
            return request.user.is_authenticated and request.user.is_admin
        else:
            return True
