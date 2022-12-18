from rest_framework.permissions import IsAuthenticated

class UserListPermission(IsAuthenticated):
    pass

class UserDetailPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and obj.pk == request.user.pk)