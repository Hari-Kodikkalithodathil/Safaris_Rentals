import csv

from django.core.management.base import BaseCommand
from vehicles.models import Vehicle


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open("vehicles.csv", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                Vehicle.objects.create(
                    name=row["name"],
                    slug=row["slug"],
                    description=row["description"],
                    seating_capacity=row["seating_capacity"],
                    daily_rate=row["daily_rate"],
                    weekly_rate=row["weekly_rate"],
                    monthly_rate=row["monthly_rate"],
                    mileage_limit=row["mileage_limit"],
                    extra_mile_cost=row["extra_mile_cost"],
                    security_deposit=row["security_deposit"],
                    status=row["status"]
                )

        self.stdout.write(
            self.style.SUCCESS("Vehicles imported successfully.")
        )