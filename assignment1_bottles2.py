#!/usr/bin/env python3

# Version 2: Command-Line Parameter

def positive_integer_check(user_input):
    """function to ensure that user has entered a positive integer
    accepts command-line parameter string
    returns a positive integer"""
    while True:
        # attempts to convert user input to integer
        try:
            value = int(user_input)
        # checks for non-integer errors
        except ValueError:
            print("***invalid input***")
            user_input = input("Please enter a positive integer (1-99): " )
            continue
        # checks for non-negative integers
        if (value < 1) or (value > 99):
            print("***invalid input***")
            user_input = input("Please enter a positive integer (1-99): " )
            continue
        else:
            break
    return value 

# import statements 
import sys

clps = sys.argv
# if no value is entered to the command-line, default to 99
if len(clps) == 1:
    number = 99
# use command-line value and do error-checks
else:
    user_input = sys.argv[1]
    # uses postivie_integer_check function above for errors
    number = positive_integer_check(user_input)

# define lyrics of song as strings
text_1 = "bottles of beer on the wall!"
text_2 = text_1[:15] + "!"
text_3 = "\nTake one down\nAnd pass it around"

# modify lyrics of song for plural to singular changes
text_4 = text_1[:6] + text_1[7:]
text_5 = text_4[:14] + "!"
text_6 = "No more"

# create desending order list with all bottle values
bottle_values = sorted(list(range(1,number+1)),reverse=True)

# loop for each verse and print bottle values with lyrics
print("") # start output with blank line
for value in bottle_values:
    # 1 bottle of beer verse
    if value == 1:
        print(value, text_4)
        print(value, text_5, text_3)
        print(text_6, text_1, "\n")
    # 2 bottles of beer verse
    elif value == 2:
        print(value, text_1)
        print(value, text_2, text_3)
        print(value-1, text_4, "\n")
    # greater than 2 bottles of beer verses
    else:
        print(value, text_1)
        print(value, text_2, text_3)
        print(value-1, text_1, "\n")
    
