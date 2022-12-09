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
    # path('<str:num>/inbody/recent/', views.inbody),
    # path('<str:num>/inbody/list/', views.inbody),
    # path('<str:num>/inbody/<int:inbody_pk>/', views.inbody_detail),
]
