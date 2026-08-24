import csv
import random
from django.utils.text import slugify

number_of_vehicles = 7

# vehicle_names = [
#     "Toyota Innova",
#     "Toyota Fortuner",
#     "Toyota Glanza",
#     "Maruti Suzuki Swift",
#     "Maruti Suzuki Baleno",
#     "Maruti Suzuki Ertiga",
#     "Hyundai i20",
#     "Hyundai Creta",
#     "Hyundai Venue",
#     "Honda City",
#     "Honda Amaze",
#     "Tata Nexon",
#     "Tata Punch",
#     "Mahindra XUV700",
#     "Mahindra Scorpio",
# ]

vehicle_names = [
    "Toyota Innova",
    "Toyota Fortuner",
    "Toyota Glanza",
    "Toyota Hyryder",
    "Toyota Rumion",

    "Maruti Suzuki Swift",
    "Maruti Suzuki Baleno",
    "Maruti Suzuki Ertiga",
    "Maruti Suzuki Brezza",
    "Maruti Suzuki Dzire",
    "Maruti Suzuki Fronx",
    "Maruti Suzuki Grand Vitara",

    "Hyundai i20",
    "Hyundai Creta",
    "Hyundai Venue",
    "Hyundai Verna",
    "Hyundai Exter",
    "Hyundai Alcazar",
    "Hyundai Aura",

    "Honda City",
    "Honda Amaze",
    "Honda Elevate",
    "Honda Jazz",

    "Tata Nexon",
    "Tata Punch",
    "Tata Harrier",
    "Tata Safari",
    "Tata Altroz",
    "Tata Tiago",
    "Tata Tigor",

    "Mahindra XUV700",
    "Mahindra Scorpio",
    "Mahindra Thar",
    "Mahindra XUV 3XO",
    "Mahindra Bolero",
    "Mahindra Bolero Neo",

    "Kia Seltos",
    "Kia Sonet",
    "Kia Carens",
    "Kia Carnival",

    "Renault Kwid",
    "Renault Triber",
    "Renault Kiger",

    "Volkswagen Polo",
    "Volkswagen Taigun",
    "Volkswagen Virtus",

    "Skoda Slavia",
    "Skoda Kushaq",
    "Skoda Kodiaq"
]

with open("vehicles.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "name",
        "slug",
        "description",
        "seating_capacity",
        "daily_rate",
        "weekly_rate",
        "monthly_rate",
        "mileage_limit",
        "extra_mile_cost",
        "security_deposit",
        "status"
    ])

    for i in range(number_of_vehicles):

        name = vehicle_names[i]
        daily_rate = random.randint(1500, 5000)

        writer.writerow([
            name,
            slugify(name),
            f"{name} rental vehicle",
            random.choice([4, 5, 7]),
            daily_rate,
            daily_rate * 6,
            daily_rate * 20,
            random.choice([150, 200, 250, 300]),
            random.choice([10, 15, 20, 25]),
            random.choice([3000, 5000, 7500, 10000]),
            random.choice(["ACTIVE", "INACTIVE"])
        ])

print(f"{number_of_vehicles} fake vehicles generated.")