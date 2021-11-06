from django.contrib.auth        import get_user_model
from rest_framework.serializers import ModelSerializer


class RegisterUserSerializer(ModelSerializer):
    # Account 모델 속성 입력창
    class Meta:
        model = get_user_model() # 커스텀한 Account 모델 가져오기(AUTH_USER_MODEL = 'accounts.Account')
        fields = '__all__' # 모든 속성들 포함
        read_only_fields = ('is_staff', 'date_of_join', 'last_login', 'is_admin', 'id') # 입력 제외
        extra_kwargs = {'password' : {'write_only' : True}} #respose 했을 때 출력 X 해주기 위해

    # UserManager의 create_user함수로 생성
    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data) # UserManager로 생성