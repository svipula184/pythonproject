import re

mobile = input("Enter Indian mobile number: ")

pattern = r'^[6-9][0-9]{9}$'

if re.match(pattern, mobile):
    print("Valid Indian mobile number")
else:
    print("Invalid Indian mobile number")