# import csv

# from django.core.management.base import BaseCommand
# from customers.models import Customer


# class Command(BaseCommand):

#     def handle(self, *args, **options):

#         with open("customers.csv", newline="") as file:
#             reader = csv.DictReader(file)

#             for row in reader:
#                 Customer.objects.create(
#                     # first_name=row["first_name"],
#                     # last_name=row["last_name"],
#                     dob=row["dob"],
#                     # email=row["email"],
#                     phone=row["phone"],
#                     driving_license_no=row["driving_license_no"]
#                 )

#         self.stdout.write(
#             self.style.SUCCESS("Customers imported successfully.")
#         )




import csv

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from customers.models import Customer


class Command(BaseCommand):

    def handle(self, *args, **options):

        User = get_user_model()

        with open("customers.csv", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:

                user = User.objects.get(
                    email=row["email"]
                )

                Customer.objects.create(
                    user=user,
                    dob=row["dob"],
                    phone=row["phone"],
                    driving_license_no=row["driving_license_no"]
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Customers imported successfully."
            )
        )