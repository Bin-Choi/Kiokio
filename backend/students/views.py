# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# simplejwt
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from .serializers import InbodySerializer, InbodyListSerializer, StudentSerializer, StudentAttendanceSerializer, StudentInbodyListSerializer
from .models import Student, Attendance, Inbody
from datetime import datetime

# cryptography
from cryptography.fernet import Fernet


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
            'grade': student.grade,
            'room': student.room,
            'number': number,
            'name': student.name,
        }
        return Response(data)

    if request.method == 'POST':
        pw = request.data['password']
        if student.password == pw:
            key = Fernet.generate_key()

            fernet = Fernet(key)
            student.key = key
            student.save()
            password = fernet.encrypt(bytes(pw,'utf-8'))
            data = {
                'id': student.pk,
                'password': password,
            }
            return Response(data)
        
        elif student.password != pw:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

@api_view(['POST'])
def inbody_list(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    pw = request.data['password']
    fernet = Fernet(student.key)
    password = fernet.decrypt(pw).decode('utf-8')
    
    if password == student.password: 
        inbodylist = Inbody.objects.filter(student=student_pk)
        serializer = InbodyListSerializer(inbodylist, many=True)
        data = serializer.data
        return Response(data)
    return Response(status=status.HTTP_401_UNAUTHRIZED)


@api_view(['PUT'])
def password_update(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    pw = request.data['password']
    fernet = Fernet(student.key)
    password = fernet.decrypt(pw).decode('utf-8')   
    new_pw = request.data['newPassword']
    check_pw = request.data['currentPassword']
    
    # 인증 여부
    if password == student.password:
        
        # 기존 비밀번호가 틀렸을 때
        if check_pw != student.password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # 비밀번호 변경
        else:
            student.password = new_pw
            student.save()
            password = fernet.encrypt(bytes(student.password,'utf-8'))
            data = {
                'id' : student.pk,
                'password' : password,
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST', 'PUT', 'DELETE'])

def inbody_detail(request,inbody_pk,student_pk):
 
    student = Student.objects.get(pk=student_pk)
    pw = request.data['password']
    fernet = Fernet(student.key)
    password = fernet.decrypt(pw).decode('utf-8')
    
    if password == student.password: 
        inbody = Inbody.objects.get(pk=inbody_pk)

        if request.method == 'POST':
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
        
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def inbody_create(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    pw = request.data['password']
    fernet = Fernet(student.key)
    password = fernet.decrypt(pw).decode('utf-8')
    
    if password == student.password: 
        serializer = InbodySerializer(data=request.data['inbody'])
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(student=student_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_401_UNAUTHORIZED)       
            
@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def students(request):

    # 추가
    if request.method == 'POST':
        # # serialzier 유효성 검사
        add_list = request.data
        serializers = []
        for i in range(len(students)):
            serializer = StudentSerializer(data=add_list[i])
            if serializer.is_valid(raise_exception=True):
                serializers.append(serializer)
        # 저장
        for serializer in serializers:
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    # 수정
    if request.method == 'PUT':
        # 수정리스트에 있는 학생들이 실제 있는지 검사
        update_list = request.data
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
     
     
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def inbody_list_class(request, grade, room):
    students = Student.objects.prefetch_related('inbody_set').filter(grade=grade, room=room)

    if request.method == 'GET':
        serializer = StudentInbodyListSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def inbody_list_name(request, name):
    students = Student.objects.prefetch_related('inbody_set').filter(name=name)

    if request.method == 'GET':
        serializer = StudentInbodyListSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def inbody_update(request):

    if request.method == 'POST':
        inbody_list = request.data
        serializers = []
        for inbody_item in inbody_list:
            # 수정일 경우
            if inbody_item.get('id'):
                inbody = get_object_or_404(Inbody, pk=inbody_item['id'])
                serializer = InbodySerializer(inbody, data=inbody_item)
            # 추가일 경우
            else:
                serializer = InbodySerializer(data=inbody_item)
            # 모든 값들의 validation 먼저확인
            if serializer.is_valid(raise_exception=True):
                serializers.append(serializer)
        # 저장
        for serializer in serializers:
            serializer.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def inbody_detail_admin(request, inbody_pk):

    inbody = get_object_or_404(Inbody, pk=inbody_pk)

    if request.method == 'PUT':
        serializer = InbodySerializer(inbody, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        inbody.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)