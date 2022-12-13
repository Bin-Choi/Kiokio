from rest_framework import serializers
from .models import Student, Inbody, Attendance


class InbodySerializer(serializers.ModelSerializer):
    total_body_water = serializers.FloatField(allow_null=True)
    protein = serializers.FloatField(allow_null=True)
    minerals = serializers.FloatField(allow_null=True)
    body_fat_mass = serializers.FloatField(allow_null=True)
    # 골격근 지방 분석(muscle-fat analysis)
    weight =serializers.FloatField(allow_null=True)
    skeletal_muscle_mass = serializers.FloatField(allow_null=True)
    # 비만 분석(obesity anaylsis)
    body_mass_index = serializers.FloatField(allow_null=True)
    percent_body_fat = serializers.FloatField(allow_null=True)
    # 인바디 점수
    inbody_score = serializers.FloatField(allow_null=True)

    class Meta:
        model = Inbody
        fields = '__all__'
        
class InbodyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inbody
        fields = ('id', 'test_date', 'age', 'height', 'weight', 'percent_body_fat')

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

# class AdminInbodyListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Inbody
#         fields = ['id', 'test_date']

class StudentInbodyListSerializer(serializers.ModelSerializer):
    inbody_set = InbodySerializer(many=True, read_only=True)

    class Meta:
        model = Student
        exclude = ('password',)