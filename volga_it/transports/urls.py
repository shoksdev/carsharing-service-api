from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TransportListCreateView, TransportRetrieveUpdateDestroyView, TransportAdminViewSet

router = SimpleRouter()
router.register(r'admin/transport', TransportAdminViewSet)

urlpatterns = [
    path('transport/', TransportListCreateView.as_view(), name='transport-list'),
    path('transport/<int:pk>/', TransportRetrieveUpdateDestroyView.as_view(), name='transport-object'),
    path('')
]
