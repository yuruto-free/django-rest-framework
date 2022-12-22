from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

app_name = 'accounts'

urlpatterns = [
    re_path('', include(router.urls)),
]