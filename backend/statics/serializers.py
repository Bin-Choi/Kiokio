from rest_framework import serializers
from .models import Machine, School

class MachineSimpleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Machine
        fields = ['name', 'image']

class MachineSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Machine
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(use_url=True)

    class Meta:
        model = School
        fields = '__all__'
