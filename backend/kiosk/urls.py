from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('accounts/', include('accounts.urls')),
    # dj_rest_auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # django authentication
    path('django/', include('django.contrib.auth.urls')),
]
