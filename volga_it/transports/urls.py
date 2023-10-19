from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TransportListCreateView, TransportRetrieveUpdateDestroyView

# router = SimpleRouter()
# router.register(r'transports', TransportViewSet)

urlpatterns = [
    path('transports/', TransportListCreateView.as_view(), name='transport-list'),
    path('transports/<int:pk>', TransportRetrieveUpdateDestroyView.as_view(), name='transport-object'),
]
