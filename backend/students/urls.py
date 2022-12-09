from django.urls import path
from . import views

urlpatterns = [
    # path('attendance/', views.attendance),
    path('<str:num>/attendance/', views.attendance),
    path('<str:num>/inbody/', views.inbody),
    path('', views.students),
    path('<int:grade>/<int:room>/', views.students_class),
    path('<str:name>/', views.students_name),
    path('attendance/<int:year>/<int:month>/<int:grade>/<int:room>/', views.attendance_class),
    path('attendance/<int:year>/<int:month>/<str:name>/', views.attendance_name),
    path('inbody/create/', views.inbody_create),
    path('<str:pk>/inbody/list/', views.inbody_list),
    path('inbody/<int:inbody_pk>/', views.inbody_detail),
    path('inbody/login/', views.inbody_login),
]
