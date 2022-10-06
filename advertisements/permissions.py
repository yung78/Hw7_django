from rest_framework.permissions import BasePermission


class IsPublisherOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:  # По необходимости request.user.is_stuff
            return True
        elif request.method == 'GET' and obj.status != 'DRAFT':
            return True
        return request.user == obj.creator
