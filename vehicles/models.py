from django.db import models

# Create your models here.

class Vehicle(models.Model):
    STATUS_CHOICES=(('ACTIVE', 'Active'),
                    ('INACTIVE','Inactive'))
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    seating_capacity=models.PositiveIntegerField()
    daily_rate=models.DecimalField(max_digits=10, decimal_places=2)
    weekly_rate=models.DecimalField(max_digits=10, decimal_places=2)
    monthly_rate=models.DecimalField(max_digits=10, decimal_places=2)
    mileage_limit=models.DecimalField(max_digits=10, decimal_places=2)
    extra_mile_cost=models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')

    def __str__(self):
        return self.name

class VehicleImage(models.Model):
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image=models.ImageField(upload_to="vehicles/images/") #This is said to dynamically create a folder named imges inside vehicles when the first image get uploaded
    caption=models.CharField(max_length=100, blank=True)
    is_primary=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.vehicle.name} - {self.caption}'

