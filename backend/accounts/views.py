# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# simplejwt
from rest_framework_simplejwt.tokens import RefreshToken

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate


# Create your views here.
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']

    # 인증된 경우 사용자 객체 반환, 없을 경우 None 반환.
    user = authenticate(username = username, password = password)

    if user is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        # simple jwt token
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)
        # 사용자 DB에 refresh_token 저장
        user.refresh_token = refresh_token
        user.save()
        # access_token 반환
        data = {
            'access': access_token
        }
        return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)
    print(user)

    if request.method == 'POST':
        # 사용자 DB에 refresh_token 삭제
        user.refresh_token = ''
        user.save()
        return Response(status=status.HTTP_200_OK)
