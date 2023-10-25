from django.urls import path

from .views import RentListAPIView

# router = SimpleRouter()
# router.register(r'transport', RentListAPIView, basename='rent')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('transport/', RentListAPIView.as_view(), name='transport_list'),
]
