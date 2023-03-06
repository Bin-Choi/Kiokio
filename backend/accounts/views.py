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

@api_view(['POST'])
def login(request): # 로그인
    username = request.data['username']
    password = request.data['password']

    if request.method == 'POST':
        user = authenticate(username = username, password = password)

        # 인증 실패
        if user is None:
            get_object_or_404(get_user_model(), username=username)      # 아이디가 없을 경우, 404 반환
            return Response(status=status.HTTP_400_BAD_REQUEST)         # 비밀번호가 틀렸을 경우, 401 반환

        # 인증 성공
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)                # refresh token 생성
        access_token = str(refresh.access_token)    # access token 생성

        user.refresh_token = refresh_token          # 사용자 DB에 refresh token 저장
        user.save()

        data = {
            'user': { 'id': user.id, 'email': user.email },
            'access': access_token,
            'refresh': refresh_token
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):    # 로그아웃
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)  # 유저 정보가 없을 경우, 404 반환

    if request.method == 'POST':
        user.refresh_token = ''     # 사용자 DB에 refresh_token 삭제
        user.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_email(request):  # 이메일 변경
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)  # 유저 정보가 없을 경우, 404 반환

    if request.method == 'PUT':
        serializer = UserEmailSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):   # 유효하지 않을 경우, 400 반환
            serializer.save()
            return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_password(request):   # 비밀번호 변경

    if request.method == 'PUT':
        old_password = request.data['old_password']
        new_password =request.data['new_password']
        confirm_password =request.data['confirm_password']

        user = authenticate(username = request.user.username, password = old_password)  # 사용자 인증

        if user is None:
            data = {
                "msg": "기존 비밀번호가 틀렸습니다."
            }
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if new_password != confirm_password:
            data = {
                "msg": "새 비밀번호가 서로 일치하지 않습니다."
            }
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = UserPasswordSerializer(user, data={'password': new_password})
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(status=status.HTTP_200_OK)
        
        data = {
                "msg": "새 비밀번호가 충분히 복잡하지 않습니다."
            }
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['POST'])
def refresh(request):   # access toekn 재발급
    User = get_user_model()
    refresh = request.data['refresh']

    if request.method == 'POST':
        try:
            decode = jwt.decode(refresh, settings.SIMPLE_JWT['SIGNING_KEY'], settings.SIMPLE_JWT['ALGORITHM'],)
            pk = decode['user_id']
            user = get_object_or_404(User, pk=pk)   # 토큰의 유저 정보 가져오기

            if user.refresh_token != refresh:       # 토큰이 유효하지 않을 시, 403 에러
                return Response(status=status.HTTP_403_FORBIDDEN)
    
            # 새로운 access 토큰 발급
            access = AccessToken.for_user(user)
            data = {
                'access': str(access)
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        
        except: # 토큰 해독 불가능 시, 403에러
            return Response(status=status.HTTP_403_FORBIDDEN)