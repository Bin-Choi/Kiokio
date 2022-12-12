from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('refresh/', views.refresh),
    path('logout/', views.logout),
    path('change/email/', views.change_email),
    path('change/password/', views.change_password),
]