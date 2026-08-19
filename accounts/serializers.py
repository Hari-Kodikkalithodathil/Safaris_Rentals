from rest_framework import serializers

class SignupSerializer(serializers.Serializer):

    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)

    first_name=serializers.CharField()
    last_name=serializers.CharField()
    dob=serializers.DateField()
    phone=serializers.CharField()
    driving_license_no=serializers.CharField()