from django.db import models

# Create your models here.

class Vehicles(models.Model):
    STATUS_CHOICES=(('ACTIVE', 'Active'),('INACTIVE','Inactive'))
    name=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    seating_capacity=models.PositiveBigIntegerField()
    daily_rate=models.PositiveBigIntegerField()
    weekly_rate=models.PositiveBigIntegerField()
    monthly_rate=models.PositiveBigIntegerField()
    mileage_limit=models.PositiveBigIntegerField()
    extra_mile_cost=models.PositiveBigIntegerField()
    security_deposit=models.PositiveBigIntegerField()
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')