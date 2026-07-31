from . models import Booking
from datetime import datetime
from django.utils import timezone
from . models import BlockedDate
from decimal import Decimal



'''Checking whether a particular vehicle is available on a particular date.
If a vehicle is avalible the function retuns true else it returns false'''

def vehicle_availability(vehicle, pickup_datetime, return_datetime, exclude_bookings=None):

    overlapping_bookings=Booking.objects.filter(
        vehicle=vehicle,
        booking_status__in=["CONFIRMED","PENDING"],
        pickup_datetime__lt=return_datetime,
        return_datetime__gt=pickup_datetime
    ).exclude(id=exclude_bookings.id)

    if overlapping_bookings.exists():
        return False
    
    return True



'''Checking whether proper dates are entered for pickup and return of vehicles'''

def validate_booking_dates(pickup_datetime, return_datetime):

    if pickup_datetime>=return_datetime:
        raise ValueError("Return date must be after pickup date")
    
    if pickup_datetime<timezone.now(): 
        raise ValueError("Pickup date cannot be in the past")
    
    return True


# print(timezone.localtime())



'''Checking whether a vehicle is not blocked. The function 'vehicle_not_blocked' returns
a true value if the vehicle is free or a false value if it is blocked'''

def vehicle_not_blocked(vehicle, pickup_datetime, return_datetime):

    blocked_periods=BlockedDate.objects.filter(
        vehicle=vehicle,
        start_date__lt=return_datetime.date(),
        end_date__gt=pickup_datetime.date()
    )

    if blocked_periods.exists():
        return  False
    
    return True




'''The function that creates an object of Booking'''

def create_booking(customer, vehicle, pickup_datetime, return_datetime,
                   subtotal, tax, deposit_paid):
    
    validate_booking_dates(pickup_datetime, return_datetime)

    if not vehicle_not_blocked(vehicle, pickup_datetime, return_datetime):
        raise ValueError("The vehicle is under maintenance")

    if not vehicle_availability(vehicle, pickup_datetime, return_datetime):
        raise ValueError("The vehicle is already booked")

    total_price=subtotal+tax

    booking=Booking.objects.create(
        customer=customer,
        vehicle=vehicle,
        pickup_datetime=pickup_datetime,
        return_datetime=return_datetime,
        subtotal=subtotal,
        tax=tax,
        total_price=total_price,
        deposit_paid=deposit_paid,
    )

    return booking




'''Creating the fucntion to update a booking'''

def update_booking(booking, vehicle, pickup_datetime, return_datetime):

    validate_booking_dates(pickup_datetime, return_datetime)

    if not vehicle_availability(vehicle, pickup_datetime, return_datetime, 
                                exclude_bookings=booking):
        raise ValueError("The vehicle is already booked during this period")

    if not vehicle_not_blocked(vehicle, pickup_datetime, return_datetime):
        raise ValueError("The vehicle is under maintenance during this period")

    # booking.customer=customer
    booking.vehicle=vehicle
    booking.pickup_datetime=pickup_datetime
    booking.return_datetime=return_datetime
    booking.save()

    return booking