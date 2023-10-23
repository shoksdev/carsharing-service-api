from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TransportCreateView, TransportRetrieveUpdateDestroyView, TransportAdminViewSet

router = SimpleRouter()
router.register(r'admin/transport', TransportAdminViewSet)

urlpatterns = [
    path('transport/', TransportCreateView.as_view(), name='transport-create'),
    path('transport/<int:pk>/', TransportRetrieveUpdateDestroyView.as_view(), name='transport-object'),
    path('', include(router.urls))
]
