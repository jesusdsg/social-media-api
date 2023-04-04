from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from api.views import PostView, PostDetailView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/posts', PostView.as_view()),
    path('v1/posts/<int:pk>/', PostDetailView.as_view()),
]
