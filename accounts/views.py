from rest_framework.generics    import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer


class RegisterAccountView(CreateAPIView):
    permission_classes = [AllowAny]     #인증 여부에 상관없이 뷰 호출을 허용
    serializer_class = RegisterUserSerializer