from rest_framework import routers # Later use: from rest_framework_nested import routers

from core.user.viewsets import UserViewSet
from core.auth.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
)
from core.insurance.viewsets import InsuranceViewSet

router = routers.SimpleRouter()

# ################### AUTH ###################### #
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# ################### USER ###################### #
router.register(r'users', UserViewSet, basename='user')

# ################### insurance ###################### #
router.register(r'insurances', InsuranceViewSet, basename='insurance')

urlpatterns = [
    *router.urls,
]
