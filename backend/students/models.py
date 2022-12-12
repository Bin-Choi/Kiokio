from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="이름")
    grade = models.IntegerField(verbose_name="학년",
        validators=[
            MaxValueValidator(9),
            MinValueValidator(1),
            ]
        )
    room = models.IntegerField(verbose_name="반",
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1),
            ]
        )
    number =  models.IntegerField(verbose_name="번호",
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1),
            ]
        )
    gender = models.CharField(max_length=10, verbose_name="성별")
    password = models.CharField(verbose_name="비밀번호", max_length=4, default="0000",
        validators=[
            MinLengthValidator(4)
            ]
        )
    key = models.BinaryField(verbose_name="패스워드 키")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['grade', 'room', 'number'], name='student_id'),
        ]


class Inbody(models.Model):
    student = models.ForeignKey(Student, verbose_name=("학생번호"), on_delete=models.CASCADE)
    # 기본 정보
    height = models.IntegerField(verbose_name="키")
    age = models.IntegerField(verbose_name="나이")
    test_date = models.DateField(verbose_name="검사일시")
    # 체성분 분석(body compositioin analysis)
    total_body_water = models.FloatField(verbose_name="체수분(L)")
    protein = models.FloatField(verbose_name="단백질(kg)")
    minerals = models.FloatField(verbose_name="무기질(kg)")
    body_fat_mass = models.FloatField(verbose_name="체지방량(kg)")
    # 골격근 지방 분석(muscle-fat analysis)
    weight = models.FloatField(verbose_name="체중(kg)")
    skeletal_muscle_mass = models.FloatField(verbose_name="골격근량(kg)")
    # 비만 분석(obesity anaylsis)
    body_mass_index = models.FloatField(verbose_name=("BMI(kg/m^2)"))
    percent_body_fat = models.FloatField(verbose_name="체지방률(%)")
    # 인바디 점수
    inbody_score = models.IntegerField(verbose_name="인바디 점수")

class Attendance(models.Model):
    student = models.ForeignKey(Student, verbose_name=("학생ID"), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)