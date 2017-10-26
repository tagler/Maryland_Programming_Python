import re

user_input = input("enter a floating point: ")

pattern = "^[+-]?\d+\.\d+$"

if re.search(pattern, user_input):
    if user_input[0] == '-':
        print("negative floating point")
    else:
        print("positive floating point")
else:
    print("not floating point")
