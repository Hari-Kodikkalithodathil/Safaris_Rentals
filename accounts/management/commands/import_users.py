import csv

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):

    help = "Import users from users.csv"

    def handle(self, *args, **options):

        with open("users.csv", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:

                User.objects.create_user(
                    # username=row["username"],
                    email=row["email"],
                    password=row["password"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                )

        self.stdout.write(
            self.style.SUCCESS("Users imported successfully.")
        )