from faker import Faker
import csv
import random
from datetime import timedelta

fake = Faker()

# --------------------------------------------------
# Read customers
# --------------------------------------------------

with open("customers.csv", newline="") as customer_file:
    customers = list(csv.DictReader(customer_file))


# --------------------------------------------------
# Read vehicles
# --------------------------------------------------

with open("vehicles.csv", newline="") as vehicle_file:
    vehicles = list(csv.DictReader(vehicle_file))


# --------------------------------------------------
# Create bookings.csv
# --------------------------------------------------

number_of_bookings = 10

with open("bookings.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "customer_email",
        "vehicle_name",
        "pickup_date",
        "return_date",
        "subtotal",
        "tax",
        "total_price",
        "deposit_paid",
        "payment_status",
        "booking_status"
    ])

    for _ in range(number_of_bookings):

        # Select an existing customer
        customer = random.choice(customers)

        # Select an existing vehicle
        vehicle = random.choice(vehicles)

        # Generate pickup and return dates
        pickup_date = fake.date_time_between(
            start_date="+1d",
            end_date="+90d"
        )

        rental_days = random.randint(1, 14)

        return_date = pickup_date + timedelta(days=rental_days)

        # Vehicle daily rate
        daily_rate = float(vehicle["daily_rate"])

        # Calculate price
        subtotal = daily_rate * rental_days

        # 18% GST
        tax = subtotal * 0.18

        total_price = subtotal + tax

        # Security deposit
        security_deposit = float(vehicle["security_deposit"])

        deposit_paid = random.choice([
            security_deposit,
            0
        ])

        # Payment status
        payment_status = random.choice([
            "PAID",
            "PENDING"
        ])

        # Booking status
        booking_status = random.choice([
            "CONFIRMED",
            "PENDING",
            "CANCELLED"
        ])

        writer.writerow([
            customer["email"],
            vehicle["name"],
            pickup_date.strftime("%Y-%m-%d %H:%M:%S"),
            return_date.strftime("%Y-%m-%d %H:%M:%S"),
            round(subtotal, 2),
            round(tax, 2),
            round(total_price, 2),
            round(deposit_paid, 2),
            payment_status,
            booking_status
        ])

print(f"{number_of_bookings} fake bookings generated.")