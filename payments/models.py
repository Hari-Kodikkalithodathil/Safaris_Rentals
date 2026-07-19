from django.db import models
from bookings.models import Booking

# Create your models here.

class Payments(models.Model):
    booking=models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    payment_method=models.CharField(max_length=50)
    status=models.CharField(max_length=50, choices=Booking.PAYMENT_STATUS, default="PENDING")
    processed_at=models.DateTimeField(auto_now_add=True)