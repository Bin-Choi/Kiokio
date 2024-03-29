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

from .serializers import InbodySerializer, InbodyListSerializer, StudentSerializer, StudentAttendanceSerializer, StudentInbodyListSerializer, InbodyStudentSerializer
from .models import Student, Attendance, Inbody
from datetime import datetime, timezone, timedelta

# cryptography
from cryptography.fernet import Fernet

KST = timezone(timedelta(hours=9))

# Create your views here.
@api_view(['GET', 'POST'])
def attendance(request, num):
    grade = int(num[0])
    room = int(num[1:3])
    number = int(num[3:5])

    student = Student.objects.get(grade=grade, room=room, number=number)

    if request.method == 'GET':
        date_time = datetime.now(KST)
        date = str(date_time)[:10]
        time = str(date_time.time())[:8]
        data = {
            'name': student.name,
            'grade': grade,
            'room': room,
            'number': number,
            'num': num,
            'date': date,
            'time': time,
        }
        return Response(data)

    elif request.method == 'POST':
        date = request.data['date']
        time = request.data['time']

        if Attendance.objects.filter(student=student, date=date).exists():
            last_attendance =  Attendance.objects.filter(student=student, date=date).order_by('-time')[0]

            time_1 = datetime.strptime(str(last_attendance.time),"%H:%M:%S")
            time_2 = datetime.strptime(time,"%H:%M:%S")
            time_interval = time_2 - time_1

            if time_interval <= timedelta(minutes=40):
                return Response(status=status.HTTP_400_BAD_REQUEST)
                     
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
        # get 요청
        if request.method == 'POST':
            serializer = InbodySerializer(inbody)
            data = serializer.data
            return Response(data)

        elif request.method == 'PUT':
            serializer = InbodySerializer(inbody, data=request.data['inbody'])
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
            serializer.save(student=student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_401_UNAUTHORIZED)       
            
@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def students(request):

    # 추가
    if request.method == 'POST':
        serializers = StudentSerializer(many=True, data=request.data)
        # 하나라도 오류나면, 저장이 진행되지 않음
        if serializers.is_valid(raise_exception=True):
            serializers.save()
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
    students = Student.objects.filter(grade=grade, room=room).order_by('grade', 'room', 'number')

    if request.method == 'GET':
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def students_name(request, name):
    students = Student.objects.filter(name=name).order_by('grade', 'room', 'number')

    if request.method == 'GET':
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_class(request, year, month, grade, room):
    students = Student.objects.prefetch_related(
        Prefetch('attendance_set', queryset=Attendance.objects.filter(date__year=year, date__month=month))
        ).filter(grade=grade, room=room).order_by('grade', 'room', 'number')

    if request.method == 'GET':
        serializer = StudentAttendanceSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_name(request, year, month, name):
    students = Student.objects.prefetch_related(
        Prefetch('attendance_set', queryset=Attendance.objects.filter(date__year=year, date__month=month))
        ).filter(name=name).order_by('grade', 'room', 'number')

    if request.method == 'GET':
        serializer = StudentAttendanceSerializer(students, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def inbody_list_class(request, start_date, end_date, grade, room):
    students = Student.objects.prefetch_related(
            Prefetch('inbody_set', queryset=Inbody.objects.filter(test_date__gte=start_date, test_date__lte=end_date).order_by('test_date'))
            ).filter(grade=grade, room=room).order_by('grade', 'room', 'number')

    if request.method == 'GET':
        serializer = StudentInbodyListSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def inbody_list_name(request, start_date, end_date, name):
    students = Student.objects.prefetch_related(
            Prefetch('inbody_set', queryset=Inbody.objects.filter(test_date__gte=start_date, test_date__lte=end_date).order_by('test_date'))
            ).filter(name=name).order_by('grade', 'room', 'number')

    if request.method == 'GET':
        serializer = StudentInbodyListSerializer(students, many=True)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def inbody_update(request):

    if request.method == 'PUT':
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
        response = []
        for serializer in serializers:
            serializer.save()
            response.append(serializer.data)
        response.sort(key=lambda x: x['test_date'])
        return Response(response, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        delete_list = request.data
        print(delete_list)
        # 삭제
        for inbody_pk in delete_list:
            inbody = get_object_or_404(Inbody, pk=inbody_pk)
            inbody.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def inbody_list_class_date(request, date, grade, room):
    inbodies = Inbody.objects.select_related('student').filter(student__grade=grade, student__room=room, test_date=date).order_by('student__number')

    if request.method == 'GET':
        serializer = InbodyStudentSerializer(inbodies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def inbody_list_name_date(request, date, name):
    inbodies = Inbody.objects.select_related('student').filter(student__name=name, test_date=date).order_by('student__grade', 'student__room', 'student__number')

    if request.method == 'GET':
        serializer = InbodyStudentSerializer(inbodies, many=True)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def inbody_list_date(request):
    # 수정
    if request.method == 'PUT':
        # 수정리스트에 있는 인바디가 실제로 있는지 검사
        update_list = request.data
        inbodies = []
        for inb in update_list:
            inbody = get_object_or_404(Inbody, pk=inb['id'])
            inbodies.append(inbody)
        # serialzier 유효성 검사
        serializers = []
        for i in range(len(inbodies)):
            serializer = InbodyStudentSerializer(inbodies[i], data=update_list[i])
            if serializer.is_valid(raise_exception=True):
                serializers.append(serializer)
        # 저장
        for serializer in serializers:
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        # 삭제리스트에 있는 인바디를 조회
        delete_list = request.data
        inbodies = []
        for pk in delete_list:
            inbody = get_object_or_404(Inbody, pk=pk)
            inbodies.append(inbody)
        # 인바디 삭제
        for inbody in inbodies:
            inbody.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)