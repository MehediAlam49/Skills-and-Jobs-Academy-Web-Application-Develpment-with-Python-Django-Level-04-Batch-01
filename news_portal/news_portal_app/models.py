from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):

    def __str__(self):
        return f'{self.username}'
    
class newsModel(models.Model):
    title=models.CharField(max_length=100, null=True)
    content=models.TextField(null=True)
    thumb_image=models.ImageField(upload_to='media/thumbnail-image', null=True)
    published_date=models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title}'