#!/usr/bin/env python3

# Assignment 2 
# Version 2: Challenge 2 (Ulam's game) 

# import statements 
import random

# define list of possible values
numbers = range(1,101)

# lie probability
lie_odds = 0.2

# randomly choose value
computer_value = random.choice(numbers) 

# output text
text_0 = "Try to guess my number: "
text_1 = "\nHello, I'm thinking of a number from 1 to 100..."
text_2 = " is too low - please guess again: "
text_3 = " is too high - please guess again: "
text_4 = " is correct!!! You guessed my number in "
text_5 = " guesses!!!"
text_6 = " is not a valid guess - please guess again: "
text_7 = "*** I lied about "
text_8 = " being too high!!! ***\n"
text_9 = " being too low!!! ***\n"
text_10 = " guess!!!"
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

# game loop, keeps track of number of guesses and if lied 
user_input = input_check( input(text_0) )
guess = 1
lie = False
lie_turn = None
while True:
    # correct guess
    if user_input == computer_value:
        break
    # incorrect guess
    else:
        # lie
        if (lie == False) and (random.random() < lie_odds):
            # less than the correct value
            if user_input < computer_value:
                lie_turn = text_7+str(user_input)+text_8
                user_input = input_check( input( str(user_input)+text_3 ) )
            # not less than (greater than) the correct value 
            else:
                lie_turn =  text_7+str(user_input)+text_9
                user_input = input_check( input( str(user_input)+text_2 ) )
            # set lie flag to only allow 1 lie per game 
            lie = True 
        # does not lie
        else:
            # less than the correct value
            if user_input < computer_value:
                user_input = input_check( input( str(user_input)+text_2 ) )
            # not less than (greater than) the correct value 
            else:
                user_input = input_check( input( str(user_input)+text_3 ) )
    # increase number of guesses counter each round
    guess += 1

# print final output of correct guess, number of gussess, and if lied 
if guess == 1:
    print( str(user_input)+text_4+str(guess)+text_10+"\n" )
elif lie_turn:
    print( str(user_input)+text_4+str(guess)+text_5 )
    print( lie_turn )
else:
    print( str(user_input)+text_4+str(guess)+text_5+"\n" )




