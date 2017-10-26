
l = [1,2,3,4,5,6,7,8,9,10]

while True:
    i = input( "please enter an index for the list: ")
    if i == "end.":
        break
    try:
        value = int(i)
        if value < 0:
            raise IndexError
        else:
            value = l[ value ]
            print( value )
    except IndexError:
        print("***invalid index value***")
    except ValueError:
        print("***invalid index type, please enter an integer***")

