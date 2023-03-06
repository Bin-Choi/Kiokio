from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password as validate

class UserEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email',]

class UserPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['password',]
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True}
        }
        
    def validate_password(self, value):
        validate(value)
        return value
