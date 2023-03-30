from django.urls import path
from . import views

urlpatterns = [
    path('machines/', views.machine),
    path('machines/<int:post_pk>/', views.machine_detail),
    path('school/', views.school),
]