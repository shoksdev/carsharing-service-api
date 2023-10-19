from django.urls import path, include

from .views import TransportListCreateView, TransportRetrieveUpdateDestroyView

urlpatterns = [
    path('transports/', TransportListCreateView.as_view(), name='transport-list'),
    path('transports/<int:pk>/', TransportRetrieveUpdateDestroyView.as_view(), name='transport-object'),
]
