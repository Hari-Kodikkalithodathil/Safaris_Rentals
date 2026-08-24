from rest_framework import serializers

from .models import CustomUser
from customers.models import Customer

class SignupSerializer(serializers.Serializer):

    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)

    first_name=serializers.CharField()
    last_name=serializers.CharField()
    dob=serializers.DateField()
    phone=serializers.CharField()
    driving_license_no=serializers.CharField()

    def validate_email(self, value):

        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists"
            )

        return value

    def validate_phone(self, value):

        if Customer.objects.filter(phone=value).exists():
            raise serializers.ValidationError(
                "A user with the same phone number exists"
            )

        return value

    def validate_driving_license_no(self, value):

        if Customer.objects.filter(driving_license_no=value).exists():
            raise serializers.ValidationError(
                "A user the same driving license number exists"
            )

        return value