from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TransportViewSet

router = SimpleRouter()
router.register(r'transports', TransportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
