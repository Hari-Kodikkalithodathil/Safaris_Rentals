from django.db import models
from customers.models import Customer
from vehicles.models import Vehicle

# Create your models here.

class Booking(models.Model):
    BOOKING_STATUS=(('CONFIRMED','Confirmed'), 
                    ('PENDING','Pending'), 
                    ('CANCELLED','Cancelled'))
    PAYMENT_STATUS=(('PAID','Paid'), 
                    ('PENDING','Pending'), 
                    ('REFUNDED','Refunded'))
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_date=models.DateTimeField()
    return_date=models.DateTimeField()
    subtotal=models.DecimalField(max_digits=10, decimal_places=2)
    tax=models.DecimalField(max_digits=10, decimal_places=2)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    deposit_paid=models.DecimalField(max_digits=10, decimal_places=2)
    payment_status=models.CharField(max_length=15, choices=PAYMENT_STATUS, default='PENDING')
    booking_status=models.CharField(max_length=15, choices=BOOKING_STATUS, default="PENDING")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} : {self.vehicle.name}'



'''The class below is for vehicles when thay become unavailable due to service, breakdowns
 etc. It is not about unavailability due to bookings'''

class BlockedDate(models.Model):
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField(blank=True)

    def __str__(self):
        return f'{self.vehicle.name} : Blocked from {self.start_date} to {self.end_date}'
    