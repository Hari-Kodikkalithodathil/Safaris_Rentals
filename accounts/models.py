from django.db import models

# Create your models here.

class AdminUser(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    role=models.CharField(max_length=25)

