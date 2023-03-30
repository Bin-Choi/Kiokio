from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('refresh/', views.refresh),
    path('change/email/', views.change_email),
    path('change/password/', views.change_password),
]