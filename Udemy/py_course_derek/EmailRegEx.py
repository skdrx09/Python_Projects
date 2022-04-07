import re

email_list = "db@aol.com m@.com @apple.com db@.com"

for e in email_list.split():
    if re.search("[\w\._%+\-]{1,20}@[\w\.\-]{1,20}\.\D{1,3}", e):
        print(f"{e} is a legitimate email address.")

print("Email matches:", len(re.findall("[\w\._%+\-]{1,20}@[\w\.\-]{1,20}\.\D{1,3}", email_list)))


# Additional Tests

phone_number = "11-6449-9695, 15 5554 3423 "

if re.findall("[\d]{2}.[\d]{4}.[\d]{4}", phone_number):
    print('It is a valid phone number')

print(re.findall("[\d]{2}.[\d]{4}.[\d]{4}", phone_number))