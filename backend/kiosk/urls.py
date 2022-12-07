from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    # dj_rest_auth
    # path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    # simplejwt token
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
