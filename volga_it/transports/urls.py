from django.urls import path, include

from .views import TransportListCreateView, TransportRetrieveUpdateDestroyView

urlpatterns = [
    path('transport/', TransportListCreateView.as_view(), name='transport-list'),
    path('transport/<int:pk>/', TransportRetrieveUpdateDestroyView.as_view(), name='transport-object'),
]
