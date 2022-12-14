from rest_framework import serializers
from .models import Student, Inbody, Attendance


class InbodySerializer(serializers.ModelSerializer):
    # required는 deserialize, allow_null은 serialize
    total_body_water = serializers.FloatField(required=False, allow_null=True)
    protein = serializers.FloatField(required=False, allow_null=True)
    minerals = serializers.FloatField(required=False, allow_null=True)
    body_fat_mass = serializers.FloatField(required=False, allow_null=True)
    # 골격근 지방 분석(muscle-fat analysis)
    weight =serializers.FloatField(required=False, allow_null=True)
    skeletal_muscle_mass = serializers.FloatField(required=False, allow_null=True)
    # 비만 분석(obesity anaylsis)
    body_mass_index = serializers.FloatField(required=False, allow_null=True)
    percent_body_fat = serializers.FloatField(required=False, allow_null=True)
    # 인바디 점수
    inbody_score = serializers.FloatField(required=False, allow_null=True)

    class Meta:
        model = Inbody
        fields = '__all__'

    # blank가 들어왔을 경우에, null로 바꿔 준다
    def to_internal_value(self, data):
        student = data.get('student')
        height = data.get('height')
        age = data.get('age')
        test_date = data.get('test_date')
        total_body_water = data.get('total_body_water')
        protein = data.get('protein')
        minerals = data.get('minerals')
        body_fat_mass = data.get('body_fat_mass')
        weight = data.get('weight')
        skeletal_muscle_mass = data.get('skeletal_muscle_mass')
        body_mass_index = data.get('body_mass_index')
        percent_body_fat = data.get('percent_body_fat')
        inbody_score = data.get('inbody_score')

        # Perform the data validation.
        if student:
            student = Student.objects.get(pk=student)
        if total_body_water == '':
            total_body_water = None
        if protein == '':
            protein = None
        if minerals == '':
            minerals = None
        if body_fat_mass == '':
            body_fat_mass = None
        if skeletal_muscle_mass == '':
            skeletal_muscle_mass = None
        if body_mass_index == '':
            body_mass_index = None
        if percent_body_fat == '':
            percent_body_fat = None
        if inbody_score == '':
            inbody_score = None

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            'student' : student,
            'height' : height,
            'age' : age,
            'test_date' : test_date,
            'total_body_water' : total_body_water,
            'protein' : protein,
            'minerals' : minerals,
            'body_fat_mass' : body_fat_mass,
            'weight' : weight,
            'skeletal_muscle_mass' : skeletal_muscle_mass,
            'body_mass_index' : body_mass_index,
            'percent_body_fat' : percent_body_fat,
            'inbody_score' : inbody_score,
        }

        
class InbodyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inbody
        fields = ('id', 'test_date', 'age', 'height', 'weight', 'percent_body_fat')

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ('key',)
        

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
        exclude = ('password', 'key')