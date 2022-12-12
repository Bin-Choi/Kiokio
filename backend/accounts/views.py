# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# simplejwt
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserEmailSerializer, UserPasswordSerializer
from django.conf import settings

import jwt


# Create your views here.
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']

    # 인증된 경우 사용자 객체 반환, 없을 경우 None 반환.
    user = authenticate(username = username, password = password)
    # 인증되지 않은 사용자라면, 회원정보 없음을 반환.
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
        # 쿠키 발행 오류. 크롬에서 쿠키저장을 막아버림 // Set-Cookie: my-app-auth=xxxxxxxxxxxxx; expires=Sat, 28 Mar 2020 18:59:00 GMT; HttpOnly; Max-Age=300; Path=/
            # response = Response()
            # response.set_cookie(key ='access', value= access_token, expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'], httponly=True,domain = 'localhost:8080')
            # access_token 반환
        # access_token, refresh_token 반환
        data = {
            'user': { 'id': user.id, 'email': user.email },
            'access': access_token,
            'refresh': refresh_token
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def refresh(request):
    pk = request.data['user_id']
    refresh = request.data['refresh']
    # 인증하려는 유저 정보 가져오기
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        # 보낸 refresh token이 해당 유저 DB의 refresh token과 동일한지 비교
        if user.refresh_token == refresh:
            # refresh token의 만료기간 확인. 만료되면 decode가 작동하지 않음
            try:
                jwt.decode(refresh, settings.SIMPLE_JWT['SIGNING_KEY'], settings.SIMPLE_JWT['ALGORITHM'],)
            # 만료했을 경우, 401에러 반환
            except jwt.ExpiredSignatureError:
                return Response(status=status.HTTP_403_FORBIDDEN)
            access = AccessToken.for_user(user)
            data = {
                'access': str(access)
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'POST':
        # 사용자 DB에 refresh_token 삭제
        user.refresh_token = ''
        user.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_email(request):
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'PUT':
        serializer = UserEmailSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_password(request):
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'PUT':
        password1 =request.data['password1']
        password2 =request.data['password2']
        if password1 != password2:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserPasswordSerializer(user, data={'password': password1})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)