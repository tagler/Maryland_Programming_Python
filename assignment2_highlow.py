#!/usr/bin/env python3

# Assignment 2 
# Version 1: Basic Requirements and Challenge 1 (input must be 1-100)

# import statements 
import random

# define list of possible values 
numbers = range(1,101)

# randomly choose value
computer_value = random.choice(numbers) 

# output text
text_0 = "Try to guess my number: "
text_1 = "\nHello, I'm thinking of a number from 1 to 100..."
text_2 = " is too low - please guess again: "
text_3 = " is too high - please guess again: "
text_4 = " is correct!!! You guessed my number in "
text_5 = " guesses!!!\n"
text_6 = " is not a valid guess - please guess again: "
text_7 = " guess!!!\n"
print(text_1)

# function to check user input for integers 1 to 100 only
# accepts a string, returns an integer
def input_check(input_value):
    # make list of valid inputs
    numbers_strings = list( map(str, numbers) )
    # loops until valid input given
    while True:
        # if not valid input, ask for input again
        if input_value not in numbers_strings:
            input_value = input( input_value+text_6 )
            continue
        # if valid input, stop loop and return int value 
        else:
            break
    return int( input_value )

# game loop
user_input = input_check( input(text_0) )
guess = 1
while True:
    # correct guess
    if user_input == computer_value:
        break
    # incorrect guess
    else:
        # less than the correct value
        if user_input < computer_value:
            user_input = input_check( input( str(user_input)+text_2 ) )
        # not less than (greater than) the correct value 
        else:
            user_input = input_check( input( str(user_input)+text_3 ) )
        # increase number of guesses counter 
        guess += 1

# print final output of correct guess and number of guesses
if guess == 1:
    print( str(user_input)+text_4+str(guess)+text_7 )
else:
    print( str(user_input)+text_4+str(guess)+text_5 )



