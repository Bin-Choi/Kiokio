from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password 

class UserEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email',]

# https://medium.com/django-rest/django-rest-framework-change-password-and-update-profile-1db0c144c0a3
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True,  validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"new_password": "새 비밀번호를 다시 확인해주세요."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "기본 비밀번호가 일치하지 않습니다."})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance
    
class UserPasswordUpdateSerializer(serializers.ModelSerializer):
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
