
l = [1,2,3,4,5,6,7,8,9,10]

while True:
    i = input( "please enter an index for the list: ")
    if i == "end.":
        break
    try:
        value = l[ int(i) ]
        print( value )
    except LookupError:
        print("invalid list index, please enter an integer in range")
    except ValueError:
        print("invalid index type, please enter an integer")
    except:
        print("unknown error") 
