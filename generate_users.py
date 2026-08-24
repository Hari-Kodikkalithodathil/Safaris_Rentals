from faker import Faker
import csv

fake = Faker()

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        # "username",
        "email",
        "password",
        "first_name",
        "last_name"
    ])

    number_of_rows = 15

    for _ in range(number_of_rows):
        writer.writerow([
            # fake.unique.user_name(),
            fake.unique.email(),
            "Test@123",
            fake.first_name(),
            fake.last_name(),
        ])

print(f"{number_of_rows} fake users generated.")