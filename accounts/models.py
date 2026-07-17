from django.db import models

# Create your models here.

class AdminUser(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    role=models.CharField(max_length=25)

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.DateField()
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15, unique=True)
    driving_license_no=models.CharField(max_length=15, unique=True)