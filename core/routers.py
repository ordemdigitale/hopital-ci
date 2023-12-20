from rest_framework import routers # Later use: from rest_framework_nested import routers

from core.user.viewsets import UserViewSet
from core.auth.viewsets import (
    RegisterViewSet,
    #LoginViewSet,
    #RefreshViewSet,
)

router = routers.SimpleRouter()

# ################### AUTH ###################### #
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

# ################### USER ###################### #
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]
