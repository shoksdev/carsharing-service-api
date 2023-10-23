from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/', include('rent.urls')),
    path('api/', include('users.urls')),
    path('api/', include('payment.urls')),
    path('api/', include('transports.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/account/', include('djoser.urls')),
    path('api/account/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api/account/signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
