import re

user_input = input("enter a line: ")

pattern = "^(\d\d[A-Z][A-Z])\s+(.*)$"

if re.search(pattern, user_input):
    print("correctly formatted!")
else:
    print("not formatted correctly")

