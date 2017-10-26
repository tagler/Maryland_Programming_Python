#!/usr/bin/env python3

# Version 3: Command-Line Parameter with Text

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

def convert(bottle_values):
    """function to convert numbers to text (1-99)
    accepts a list of integers 
    returns a list of text strings"""
    # dictionary for 1-digit numbers and exceptions conversions 
    numbers_1d  = { '0' : "",
                    '1' : "one",
                    '2' : "two",
                    '3' : "three",
                    '4' : "four",
                    '5' : "five",
                    '6' : "six",
                    '7' : "seven",
                    '8' : "eight",
                    '9' : "nine",
                    '10' : "ten",
                    '11' : "eleven",
                    '12' : "twelve",
                    '13' : "thirteen",
                    '14' : "fourteen",
                    '15' : "fifthteen",
                    '16' : "sixteen",
                    '17' : "seventeen",
                    '18' : "eightteen",
                    '19' : "nineteen",
                    '20' : "twenty",
                    '30' : "thirty",
                    '40' : "forty",
                    '50' : "fifty",
                    '60' : "sixty",
                    '70' : "seventy",
                    '80' : "eighty",
                    '90' : "ninety" }
    # dictionary for 2-digit number conversions
    numbers_2d = { '2' : "twenty-",
                   '3' : "thirty-",
                   '4' : "forty-",
                   '5' : "fifty-",
                   '6' : "sixty-",
                   '7' : "seventy-",
                   '8' : "eighty-",
                   '9' : "ninety-" }
    # empty list for converted text
    bottle_text = []
    # loop for each number value
    for each_value in bottle_values:
        # convert integer to string for lookup dictionary
        each_value_str = str(each_value)
        # convert single digits and exceptions
        if each_value_str in numbers_1d:
            bottle_text.append( numbers_1d[each_value_str] )
        # convert 2-digit numbers 
        else:
            # separate into first digit and second digit
            first_digit = each_value_str[0]
            second_digit = each_value_str[1]
            # combine first and second digit lookups
            text_string = numbers_2d[first_digit] + numbers_1d[second_digit]
            bottle_text.append( text_string )
    return bottle_text

# import statements 
import sys
import string

# get command-line parameter from user, only uses first parameter
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

# convert all numbers in list to text using convert function above
bottle_text = convert(bottle_values)

# loop for each verse and print bottle number text with lyrics
print("") # start output with blank line
for index,value in enumerate(bottle_text):
    # 1 bottle of beer verse
    if value == "one":
        print(value[0].upper()+value[1:], text_4)
        print(value[0].upper()+value[1:], text_5, text_3)
        print(text_6, text_1, "\n")
    # 2 bottles of beer verse
    elif value == "two":
        print(value[0].upper()+value[1:], text_1)
        print(value[0].upper()+value[1:], text_2, text_3)
        text_7 = bottle_text[index+1][0].upper()+bottle_text[index+1][1:]
        print(text_7, text_4, "\n")
    # greater than 2 bottles of beer verses
    else:
        print(value[0].upper()+value[1:], text_1)
        print(value[0].upper()+value[1:], text_2, text_3)
        text_8 = bottle_text[index+1][0].upper()+bottle_text[index+1][1:]
        print(text_8, text_1, "\n")
    
