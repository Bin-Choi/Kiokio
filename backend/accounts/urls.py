from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('refresh/', views.refresh),
    path('logout/', views.logout),
]