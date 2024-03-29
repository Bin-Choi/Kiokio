from django.urls import path
from . import views

urlpatterns = [
    # path('attendance/', views.attendance),
    path('<str:num>/attendance/', views.attendance),
    path('<str:num>/inbody/', views.inbody),
    path('<int:student_pk>/inbody/create/', views.inbody_create),
    path('<int:student_pk>/inbody/list/', views.inbody_list),
    path('<int:student_pk>/inbody/<int:inbody_pk>/', views.inbody_detail),
    path('<int:student_pk>/password/', views.password_update),

    # 학생관리
    path('', views.students),
    path('<int:grade>/<int:room>/', views.students_class),
    path('<str:name>/', views.students_name),
    # 출결관리
    path('<int:year>/<int:month>/<int:grade>/<int:room>/attendance/', views.attendance_class),
    path('<int:year>/<int:month>/<str:name>/attendance/', views.attendance_name),
    # 인바디 관리
    path('<str:start_date>/<str:end_date>/<int:grade>/<int:room>/inbody/admin/', views.inbody_list_class),
    path('<str:start_date>/<str:end_date>/<str:name>/inbody/admin/', views.inbody_list_name),
    path('inbody/list/admin/', views.inbody_update),
    path('inbody/<int:inbody_pk>/admin/', views.inbody_detail_admin),
    path('inbody/list/date/', views.inbody_list_date),
    path('<str:date>/<int:grade>/<int:room>/inbody/admin/date/', views.inbody_list_class_date),
    path('<str:date>/<str:name>/inbody/admin/date/', views.inbody_list_name_date),
]
