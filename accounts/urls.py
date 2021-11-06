from django.urls import path
from .views import RegisterAccountView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('/signup', RegisterAccountView.as_view(), name='registration'),
    path('/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]