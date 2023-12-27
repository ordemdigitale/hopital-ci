from django.urls import path

from core.auth.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)

urlpatterns = [
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='auth-login'),
    path('jwt/refresh/', CustomTokenRefreshView.as_view(), name='auth-refresh'),
    path('jwt/verify/', CustomTokenVerifyView.as_view(), name='auth-verify'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
]
