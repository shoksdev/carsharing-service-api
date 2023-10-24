from django.urls import path, include
from rest_framework.routers import SimpleRouter
from djoser.views import TokenDestroyView

from .views import AccountAdminViewSet, RetrieveAccountAPIView, UpdateAccountAPIView, RegisterAccountViewSet

router = SimpleRouter()
router.register(r'admin/account', AccountAdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('account/me/', RetrieveAccountAPIView.as_view()),
    path('account/update/', UpdateAccountAPIView.as_view()),
    path('account/signup/', RegisterAccountViewSet.as_view({'post': 'create'})),
    path('account/signout/', TokenDestroyView.as_view(), name='token-destroy'),
]
