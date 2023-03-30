# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Machine, School
from .serializers import MachineSerializer, MachineSimpleSerializer, SchoolSerializer

# Create your views here.
@api_view(['GET'])
def machine(request):
    machines = Machine.objects.all()

    if request.method == 'GET':
        serializer = MachineSimpleSerializer(machines, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def machine_detail(request, machine_pk):
    machine = Machine.objects.get(pk=machine_pk)

    if request.method == 'GET':
        serializer = MachineSerializer(machine)
        return Response(serializer.data)

    if request.user.is_authenticated:
        if request.method == 'PUT':
            serializer = MachineSerializer(machine, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        if request.method == 'DELETE':
            machine.delete()
            return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT'])
def school(request):
    school = School.objects.get()

    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SchoolSerializer(school, data=request.data)
        serializer.save()
        return Response(serializer.data)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

