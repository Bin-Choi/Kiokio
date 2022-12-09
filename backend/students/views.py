# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# simplejwt
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from .serializers import InbodySerializer, InbodyListSerializer, StudentSerializer, StudentAttendanceSerializer
from .models import Student, Attendance, Inbody
from datetime import datetime

# Create your views here.
@api_view(['GET', 'POST'])
def attendance(request, num):
    grade = int(num[0])
    room = int(num[1:3])
    number = int(num[3:5])

    student = Student.objects.get(grade=grade, room=room, number=number)

    if request.method == 'GET':
        data = {
            'name': student.name,
            'grade': grade,
            'room': room,
            'number': number,
            'num': num,
            'date': datetime.today().date(),
            'time': datetime.now().time(),
        }
        return Response(data)

    elif request.method == 'POST':
        date = request.data['date']
        time = request.data['time']
        attendance = Attendance(student=student, date=date, time=time)
        attendance.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def inbody(request, num):
    grade = int(num[0])
    room = int(num[1:3])
    number = int(num[3:5])

    student = Student.objects.get(grade=grade, room=room, number=number)

    if request.method == 'GET':
        data = {
            'pk': student.pk,
            'grade': student.grade,
            'room': student.room,
            'number': number,
            'name': student.name,     
        }
        return Response(data)

    if request.method == 'POST':

        pw = request.data['password']
        pk = request.data['pk']

        if student.password == pw:
            inbodylist = Inbody.objects.filter(student=pk)
            inbody = inbodylist.order_by('-pk')[0]
            serializer = InbodySerializer(inbody)
            data = serializer.data
            return Response(data)

@api_view(['GET'])
def inbody_list(request, pk):

    if request.method == 'GET':
        pk = pk
        inbodylist = Inbody.objects.filter(student=pk)
        serializer = InbodyListSerializer(inbodylist, many=True)
        data = serializer.data
        return Response(data)

@api_view(['GET', 'PUT', 'DELETE'])
def inbody_detail(request,inbody_pk):

    inbody_pk = inbody_pk
    inbody = Inbody.objects.get(pk=inbody_pk)

    if request.method == 'GET':
        serializer = InbodySerializer(inbody)
        data = serializer.data
        return Response(data)

    elif request.method == 'PUT':
        serializer = InbodySerializer(inbody, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'DELETE':
        inbody.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def inbody_create(request):
    if request.method == 'POST':
        serializer = InbodySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
# ### 로그인 토큰발급
@api_view(['POST'])
def inbody_login(request):
    student_pk = request.data['pk']
    student = Student.objects.get(pk=student_pk)
    password = request.data['password']
    # 인증된 경우 사용자 객체 반환, 없을 경우 None 반환.
    if student.password == password:
        print("pass_ok")
        refresh = RefreshToken.for_user(student)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)
        # 사용자 DB에 refresh_token 저장
        student.refresh_token = refresh_token
        student.save()
        # access_token 반환
        data = {
            'access': access_token
        }
        return Response(data, status=status.HTTP_200_OK)

    elif student.password != password:
        print("pass_fail")
        return Response(status=status.HTTP_404_NOT_FOUND)


        # simple jwt token

# # @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# # def logout(request):
# #     User = get_user_model()
# #     user = get_object_or_404(User, pk=request.user.pk)
# #     print(user)

# #     if request.method == 'POST':
# #         # 사용자 DB에 refresh_token 삭제
# #         user.refresh_token = ''
# #         user.save()
# #         return Response(status=status.HTTP_200_OK)

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def students(request):

    if request.method == 'POST':
        serializer = StudentSerializer(many=True, data=request.data)
        
    if request.method == 'PUT':
        # 수정리스트에 있는 학생들 조회
        update_list = request.data
        print(request.data)
        students = []
        for stu in update_list:
            student = get_object_or_404(Student, pk=stu['id'])
            students.append(student)
        # serialzier 유효성 검사
        serializers = []
        for i in range(len(students)):
            serializer = StudentSerializer(students[i], data=update_list[i])
            if serializer.is_valid(raise_exception=True):
                serializers.append(serializer)
        # 저장
        for serializer in serializers:
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        # 삭제리스트에 있는 학생들 조회
        delete_list = request.data
        students = []
        for pk in delete_list:
            student = get_object_or_404(Student, pk=pk)
            students.append(student)
        # 학생 삭제
        for student in students:
            student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def students_class(request, grade, room):
    students = Student.objects.filter(grade=grade, room=room)

    if request.method == 'GET':
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def students_name(request, name):
    students = Student.objects.filter(name=name)

    if request.method == 'GET':
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_class(request, year, month, grade, room):
    students = Student.objects.prefetch_related(
        Prefetch('attendance_set', queryset=Attendance.objects.filter(date__year=year, date__month=month))
        ).filter(grade=grade, room=room)

    if request.method == 'GET':
        serializer = StudentAttendanceSerializer(students, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_name(request, year, month, name):
    students = Student.objects.prefetch_related(
        Prefetch('attendance_set', queryset=Attendance.objects.filter(date__year=year, date__month=month))
        ).filter(name=name)

    if request.method == 'GET':
        serializer = StudentAttendanceSerializer(students, many=True)
        return Response(serializer.data)
     