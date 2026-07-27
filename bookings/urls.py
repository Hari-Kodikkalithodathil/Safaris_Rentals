from django.urls import path
from .views import BookingAPIView

urlpatterns=[
    path('bookings', BookingAPIView.as_view()),
]