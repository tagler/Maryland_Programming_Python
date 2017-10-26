#!/usr/bin/env python3

# Version 1: Basic Requirements 

# define starting number of bottles of beer
number = 99

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
    
