from rest_framework import routers # Later use: from rest_framework_nested import routers

from core.auth.viewsets import RegisterViewSet
from core.insurance.viewsets import InsuranceViewSet

router = routers.SimpleRouter()

# ################### AUTH ###################### #
router.register(r'auth/users', RegisterViewSet, basename='auth-register')

# ################### insurance ###################### #
router.register(r'insurances', InsuranceViewSet, basename='insurance')

urlpatterns = [
    *router.urls,
]
