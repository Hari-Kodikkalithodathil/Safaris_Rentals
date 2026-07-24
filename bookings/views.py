from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal

from customers.models import Customer
from vehicles.models import Vehicle
from .serializers import BookingSerializer
from .services import create_booking

# Create your views here.

class BookingAPIView(APIView):

    def post(self, request):
        serializer=BookingSerializer(data=request.data)

        if  not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        data=serializer.validated_data

        try:
            customer=Customer.objects.get(id=data["customer_id"])
        except Customer.DoesNotExist:
            return Response(
                {"error" : "Customer not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            vehicle=Vehicle.objects.get(id=data["vehicle_id"])
        except Vehicle.DoesNotExist:
            return Response({"error" : "Vehicle not found"},
                            status=status.HTTP_404_NOT_FOUND)


        
        '''Hardcoding price calculation value for temporary testing'''

        subtotal=Decimal("1000.00")
        tax=Decimal("180.00")
        deposit_paid=Decimal("5000.00")



        try:
            booking=create_booking(customer,vehicle,data['pickup_datetime'],data["return_datetime"],
                           subtotal,tax,deposit_paid)

            return Response(
                {"message":"Booking successful",
                 "booking_id":booking.id},
                 status=status.HTTP_201_CREATED
            )

        except ValueError as e:
            return Response(
                {"error":str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )