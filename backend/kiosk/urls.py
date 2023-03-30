from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('accounts/', include('accounts.urls')),
    path('statics/', include('statics.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # # dj_rest_auth
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # # django authentication
    # path('django/', include('django.contrib.auth.urls')),