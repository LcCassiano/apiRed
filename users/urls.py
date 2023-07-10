from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

app_name='users'

router = DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]