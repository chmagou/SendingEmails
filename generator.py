from faker import Faker
import csv

fake = Faker()

with open("info_file.csv", mode='w') as file:
    print("Started writing...")
    email_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL )
    for _ in range(1000000):
        print("Email generated...")
        email_writer.writerow([fake.email()])
        print("Email wrote!")

file.close()