from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import AccountAdminViewSet, AccountAPIView

router = SimpleRouter()
router.register(r'admin/account', AccountAdminViewSet)

urlpatterns = [
    path('account/me/', AccountAPIView.as_view()),
    path('', include(router.urls))
]
