from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import RentListAPIView, RentMyHistoryAPIView, AdminRentTransportHistoryAPIView, AdminRentViewSet, \
    AdminRentUserHistoryAPIView, rent_end_admin, rent_end, RentTransportHistoryAPIView

router = SimpleRouter()
router.register(r'admin/rent', AdminRentViewSet, basename='admin-rent')

urlpatterns = [
    path('', include(router.urls)),
    path('transporthistory/<int:pk>/', RentTransportHistoryAPIView.as_view(), name='transport_history'),
    path('rent/end/<int:pk>/', rent_end, name='transport_end'),
    path('admin/rent/end/<int:pk>/', rent_end_admin, name='transport_end_admin'),
    path('admin/transporthistory/<int:pk>/', AdminRentTransportHistoryAPIView.as_view(),
         name='transport_history_admin'),
    path('admin/userhistory/<int:pk>/', AdminRentUserHistoryAPIView.as_view(), name='user_history_admin'),
    path('rent/myhistory/', RentMyHistoryAPIView.as_view(), name='my_history'),
    path('rent/transport/', RentListAPIView.as_view(), name='transport_list'),
]
