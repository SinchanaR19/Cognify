import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return re.match(pattern, email) is not None

user_email = input("Enter your email address: ")

if is_valid_email(user_email):
    print("Valid Email Address.")
else:
    print("Invalid Email Address.")