from django.contrib import admin
from .models import Student, Inbody, Attendance

# Register your models here.
admin.site.register(Student)
admin.site.register(Inbody)
admin.site.register(Attendance)
