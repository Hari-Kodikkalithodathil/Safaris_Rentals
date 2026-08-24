import csv
from pathlib import Path

from django.core.management.base import BaseCommand

from bookings.models import Booking
from customers.models import Customer
from vehicles.models import Vehicle


class Command(BaseCommand):

    help = "Import bookings from bookings.csv"

    def handle(self, *args, **kwargs):

        csv_file = Path("bookings.csv")

        if not csv_file.exists():
            self.stdout.write(
                self.style.ERROR("bookings.csv not found.")
            )
            return

        with open(csv_file, newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                try:
                    # Find customer using email
                    customer = Customer.objects.get(
                        user__email=row["customer_email"]
                    )

                    # Find vehicle using vehicle name
                    vehicle = Vehicle.objects.get(
                        name=row["vehicle_name"]
                    )

                    # Create booking
                    Booking.objects.create(
                        customer=customer,
                        vehicle=vehicle,
                        pickup_datetime=row["pickup_date"],
                        return_datetime=row["return_date"],
                        subtotal=row["subtotal"],
                        tax=row["tax"],
                        total_price=row["total_price"],
                        deposit_paid=row["deposit_paid"],
                        payment_status=row["payment_status"],
                        booking_status=row["booking_status"]
                    )

                except Customer.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Customer not found: {row['customer_email']}"
                        )
                    )

                except Vehicle.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Vehicle not found: {row['vehicle_name']}"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS("Bookings imported successfully.")
        )