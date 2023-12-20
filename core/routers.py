from rest_framework import routers # Later use: from rest_framework_nested import routers

from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()

# ################### USER ###################### #
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]
