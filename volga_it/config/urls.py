from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('api/', include('rent.urls')),
    path('api/', include('users.urls')),
    path('api/payment/', include('payment.urls')),
    path('api/', include('transports.urls')),
    path('accounts/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api/account/signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += doc_urls
