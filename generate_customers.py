# from faker import Faker
# import csv

# fake = Faker()

# with open("customers.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow([
#         # "first_name",
#         # "last_name",
#         "dob",
#         # "email",
#         "phone",
#         "driving_license_no"
#     ])

#     number_of_rows=5

#     for _ in range(number_of_rows):
#         writer.writerow([
#             # fake.first_name(),
#             # fake.last_name(),
#             fake.date_of_birth(minimum_age=18, maximum_age=70),
#             # fake.unique.email(),
#             fake.unique.numerify("##########"),
#             fake.unique.bothify("??########")
#         ])

# print(number_of_rows," fake customers generated.")



from faker import Faker
import csv

fake = Faker()

with open("users.csv", newline="") as user_file:
    users = list(csv.DictReader(user_file))

with open("customers.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "email",
        "dob",
        "phone",
        "driving_license_no"
    ])

    for user in users:
        writer.writerow([
            user["email"],
            fake.date_of_birth(minimum_age=18, maximum_age=70),
            fake.unique.numerify("##########"),
            fake.unique.bothify("??########")
        ])

print(len(users), "fake customers generated.")