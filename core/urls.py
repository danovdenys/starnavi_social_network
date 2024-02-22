from core.viewsets import UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
from core.decorators import log_login_view



router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', log_login_view(
        ObtainAuthToken.as_view()
        ), name='login')
]