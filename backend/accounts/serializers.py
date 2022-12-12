from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email',]

class UserPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['password',]
        
    validate_password = make_password