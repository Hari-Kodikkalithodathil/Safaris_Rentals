from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.Serializer):
    vehicle_id=serializers.IntegerField()
    pickup_datetime=serializers.DateTimeField()
    return_datetime=serializers.DateTimeField()

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"
