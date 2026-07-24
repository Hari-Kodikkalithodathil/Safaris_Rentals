from rest_framework import serializers

class BookingSerializer(serializers.Serializer):
    customer_id=serializers.IntegerField
    vehicle_id=serializers.IntegerField
    pickup_datetime=serializers.DateTimeField
    return_datetime=serializers.DateTimeField
