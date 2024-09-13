from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email','first_name','last_name','birth_date' ]

    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("사용 중인 이메일입니다.")
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("사용 중인 username입니다.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PasswordCheckSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

# SubUsernameSerializer 은 구독중인 username 만 보이기 위한 용도
# 아래 SubSerializer 는 SubUsernameSerializer 의 정보를 받아 사용
class SubUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
class SubSerializer(serializers.ModelSerializer):
    subscribings = SubUsernameSerializer(many=True, read_only=True)  # 구독 중인 사용자들

    class Meta:
        model = User
        fields = ['subscribings']

# -------------------------------------------ㄱ
# 비밀번호 찾는 이메일 보내기 시리얼라이저 
class PwEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=64)

    def validate_email(self, value):
        '''데이터베이스에 존재하는지 확인'''
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("존재하지 않는 이메일입니다.")
        else:
            return value
# -------------------------------------------ㄱ


# 비밀번호 변경 시리얼라이저
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



# -------------------------------------------ㄱ
# username 찾기 시리얼라이저
class UsernameFindSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64,required=True)
# -------------------------------------------ㄱ

