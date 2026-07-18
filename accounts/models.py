from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass

class AdminProfile(models.Model):
    custom_user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role=models.CharField(max_length=25)

    def __str__(self):
        return f'{self.custom_user.first_name} {self.custom_user.last_name}'