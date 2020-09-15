from django.urls import path, include
from . import views

from rest_framework import routers, serializers, viewsets
from .views import TagListView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tags/', TagListView.as_view(), name='tags'),
]