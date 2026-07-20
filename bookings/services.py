from . models import Booking

def check_vehicle_availability(vehicle, pickup_datetime, return_datetime):
    overlapping_bookings=Booking.objects.filter(
        vehicle=vehicle,
        booking_status__in=["CONFIRMED","PENDING"],
        pickup_date__lt=return_datetime,
        return_date__gt=pickup_datetime
    )

    if overlapping_bookings.exists():
        return False
    
    return True