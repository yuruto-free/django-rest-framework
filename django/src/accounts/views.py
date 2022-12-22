from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserListSerializer

User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_staff=False, is_active=True)
    serializer_class = UserListSerializer