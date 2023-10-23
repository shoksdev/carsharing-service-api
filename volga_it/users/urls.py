from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import AccountAdminViewSet

router = SimpleRouter()
router.register(r'admin/account', AccountAdminViewSet)

urlpatterns = [
    path('', include(router.urls))
]
