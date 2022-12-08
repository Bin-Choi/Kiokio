from django.urls import path
from . import views

urlpatterns = [
    # path('attendance/', views.attendance),
    path('<str:num>/attendance/', views.attendance),
    path('<str:num>/inbody/', views.inbody),
    # path('<str:num>/inbody/recent/', views.inbody),
    path('<str:pk>/inbody/list/', views.inbody_list),
    path('inbody/<int:inbody_pk>/', views.inbody_detail),
]
