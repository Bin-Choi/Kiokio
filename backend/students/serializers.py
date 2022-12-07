from rest_framework import serializers
from .models import Student, Inbody


class InbodySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inbody
        fields = '__all__'