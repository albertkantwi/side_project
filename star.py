print("Please enther the following infomation:")
print()

first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email Address: ")
phone_number = input("Phone Number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")

print("\n The ID Card is:")
print("--------------------------------------")

print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {id_number}")
print()
print(f"{email.lower()}")
print(f"{phone_number}")

print("--------------------------------------")