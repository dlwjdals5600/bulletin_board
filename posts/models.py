from django.db   import models
from django.conf import settings

account = settings.AUTH_USER_MODEL

class Post(models.Model):
    author     = models.ForeignKey(account, on_delete=models.SET_NULL, null=True)
    title      = models.CharField(max_length=255)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'