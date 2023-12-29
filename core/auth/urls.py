from django.urls import path, re_path

from core.auth.views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)

urlpatterns = [
    re_path(r'^o/(?P<provider>\S+)/$', CustomProviderAuthView.as_view(), name='auth-provider'),
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='auth-login'),
    path('jwt/refresh/', CustomTokenRefreshView.as_view(), name='auth-refresh'),
    path('jwt/verify/', CustomTokenVerifyView.as_view(), name='auth-verify'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
]
