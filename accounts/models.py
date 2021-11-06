from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password, gender):
        if not email:
            raise ValueError("이메일은 필수로 입력하셔야 합니다.")
        
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password,
            gender = gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email=email,
            password=password,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    date_of_join = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=3,null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "accounts"