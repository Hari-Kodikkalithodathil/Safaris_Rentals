from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal

from customers.models import Customer
from vehicles.models import Vehicle
from .serializers import BookingSerializer
from .services import create_booking, update_booking
from .models import Booking
from .serializers import BookingListSerializer

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


        
        '''Hardcoding price calculation values for temporary testing'''

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


    def get(self, request, id=None):

        if id is None:
            bookings=Booking.objects.all()
            serializer=BookingListSerializer(bookings, many=True)
            return Response(serializer.data)

        try:
            bookings=Booking.objects.get(id=id)

        except Booking.DoesNotExist:
            return Response(
                {"error": "Booking not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer=BookingListSerializer(bookings)
        return Response(serializer.data)



    def put(self, request, id):

        try:
            booking=Booking.objects.get(id=id)

        except Booking.DoesNotExist:
            return Response(
                {"error": "Booking does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer=BookingSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

        data=serializer.validated_data

        try:
            customer=Customer.objects.get(id=serializer.validated_data["customer_id"])
            vehicle=Vehicle.objects.get(id=data["vehicle_id"])

        except Customer.DoesNotExist:
            return Response(
                {"error":"No such customer exists"},
                status=status.HTTP_404_NOT_FOUND
            )

        except Vehicle.DoesNotExist:
            return Response(
                {"error":"No such vehicle exists"},
                status=status.HTTP_404_NOT_FOUND
                )

        pickup_datetime=data["pickup_datetime"]
        return_datetime=data["return_datetime"]

        try:
            updated_booking=update_booking(booking, vehicle, pickup_datetime, return_datetime)

        except ValueError as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer=BookingSerializer(updated_booking)

        return Response(serializer.data)

        # if not update_booking(customer, vehicle, pickup_date, return_date):
        #     return Response("error": "The vehicle is unavailable during this period")

        