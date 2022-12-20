from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from rest_social_auth.views import SimpleJWTAuthMixin
from .permissions import UserListPermission, UserDetailPermission
from .serializers import UserListSerializer, UserDetailSerializer

User = get_user_model()

class UserViewSet(SimpleJWTAuthMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        seiralizer_class = UserListSerializer if self.action == 'list' else UserDetailSerializer

        return seiralizer_class

    def get_permissions(self):
        self.permission_classes = [UserListPermission] if self.action == 'list' else [UserDetailPermission]

        return super().get_permissions()
