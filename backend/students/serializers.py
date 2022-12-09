from rest_framework import serializers
from .models import Student, Inbody, Attendance


class InbodySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inbody
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['date', 'time']

class StudentAttendanceSerializer(serializers.ModelSerializer):
    attendance_set = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'grade', 'room', 'number', 'attendance_set']