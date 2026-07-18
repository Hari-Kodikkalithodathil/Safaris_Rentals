from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.DateField()
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15, unique=True)
    driving_license_no=models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CustomerAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)