import re

user_input = input("enter an integer: ")

pattern = "^[+-]?\d+$"

if re.search(pattern, user_input):
    if user_input[0] == '-':
        print("negative integer")
    else:
        print("positive integer")
else:
    print("not digits")

