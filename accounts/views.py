from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer,PasswordCheckSerializer, SubSerializer, ChangePasswordSerializer, UsernameFindSerializer,PwEmailSerializer
from rest_framework import generics,mixins
from rest_framework.generics import ListAPIView
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model() # 필수 지우면 큰일남

class SignupAPIView(APIView): # 회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView): # 로그아웃
    def post(self, request):
        refresh = request.data.get("refresh")
        if refresh is None:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteAPIView(APIView): # 회원탈퇴
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        serializer = PasswordCheckSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            user = authenticate(username=request.user.username, password=password)
            if user is not None:
                user.soft_delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Mypage(ListAPIView): # 마이 페이지
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        my_page = get_object_or_404(User, username=username)
        if my_page == request.user:
            serializer = UserSerializer(my_page)
            sub_serializer = SubSerializer(my_page)
            return Response({'내 정보':serializer.data, '구독중인 사람':sub_serializer.data},status=200)
        return Response({"message": "다시 시도"}, status=400)
    

class SubscribeView(APIView):  # 구독 기능
    permission_classes = [IsAuthenticated]
    def post(self, request, username):
        # 구독 대상 사용자 조회
        user = get_object_or_404(User, username=username)
        me = request.user
        # 내가 대상 사용자를 이미 구독하고 있는지 확인
        if me in user.subscribes.all():
            user.subscribes.remove(me)
            return Response("구독취소를 했습니다.", status=status.HTTP_200_OK)
        else:
            user.subscribes.add(me)
            return Response("구독했습니다.", status=status.HTTP_200_OK)
        
# password 변경
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        print(serializer)  # 디버깅용

        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                return Response({'message': '비밀번호를 성공적으로 변경하였습니다.'}, status=200)
            return Response({'error': '비밀번호가 같습니다 새 비밀번호를 입력해주세요'}, status=400)
        return Response(serializer.errors, status=400)
    

# -------------------------------------------------------------
# username 찾기
class UsernameFindAPIView(APIView):    
    @permission_classes([AllowAny])
    def put(self, request):
        serializer = UsernameFindSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(first_name=serializer.data['first_name'], last_name=serializer.data['last_name'], birth_date=serializer.data['birth']) :
                result= User.objects.get(first_name=serializer.data['first_name'], last_name=serializer.data['last_name'], birth_date=serializer.data['birth'])
                return Response("사용자님의 username은 '" + result.username + "' 입니다")
            else:
                return Response('해당 정보로 존재하는 계정이 없습니다')
        return Response('정보가 모두 입력되지 않았습니다. 다시 입력하세요')

