from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from customers .models import Customer
from .models import CustomUser
from .serializers import SignupSerializer
from django.shortcuts import render

# Create your views here.

class SignupAPIView(APIView):

    permission_classes=[AllowAny]

    def post(self, request):

        serializer=SignupSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        data=serializer.validated_data

        user=CustomUser.objects.create_user(
            email=data["email"],
            password=data["password"]
        )

        customer=Customer.objects.create(
            user=user,
            dob=data["dob"],
            phone=data["phone"],
            driving_license_no=data["driving_license_no"]
        )

        return Response(
            {
                "message":"Signup Successful",
            },
            status=status.HTTP_201_CREATED
        )