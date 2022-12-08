from rest_framework import serializers
from .models import Student, Inbody


class InbodySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inbody
        fields = '__all__'


class InbodyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inbody
        fields = ('pk', 'test_date', 'age', 'height', 'weight', 'percent_body_fat')
