from django.urls import path, include
from . import views

from rest_framework import routers, serializers, viewsets
#from .views import TagListView
from .views import tag_list, tag_details



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tag-details/<int:id>', views.tag_details, name='tag_details'),
    #path('tags/', TagListView.as_view(), name='tags'),
]