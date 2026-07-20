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
    ADDRESS_TYPES=(('RESIDENCE', 'Residence Address'),
                   ('PERMANENT', 'Permanent Address'),
                   ('OFFICE', 'Office Address'))
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin_code=models.CharField(max_length=10)
    address_type=models.CharField(max_length=10, choices=ADDRESS_TYPES, default='RESIDENCE')

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} - {self.city}'