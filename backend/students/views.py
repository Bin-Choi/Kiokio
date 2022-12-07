# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Student, Attendance, Inbody
from datetime import datetime

from .serializers import InbodySerializer, InbodyListSerializer

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
            'pk': student.pk
            
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


@api_view(['GET'])
def inbody_detail(request,inbody_pk):

    if request.method == 'GET':
        inbody_pk = inbody_pk
        inbody = Inbody.objects.get(pk=inbody_pk)
        serializer = InbodySerializer(inbody)
        data = serializer.data
        return Response(data)

