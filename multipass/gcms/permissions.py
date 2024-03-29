from rest_framework import permissions
from .views import DSListCreate

class DisableOptionsPermission(permissions.BasePermission):
    """
    Global permission to disallow all requests for method OPTIONS.
    """

    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return False
        return True