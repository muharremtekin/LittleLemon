from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Manager').exists())

class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Delivery Crew').exists())

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.groups.filter(name__in=['Manager', 'Delivery Crew']).exists() and not request.user.is_staff)
