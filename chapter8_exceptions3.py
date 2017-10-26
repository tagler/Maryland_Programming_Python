
l = []

while True:
    try:
        i = input( "please enter an integer (q to quit): ")
        if i == "q":
            break
        value = int(i)
        l.append(value)
    except KeyboardInterrupt:
        print("please do not use CTRL-C to quit, type q to quit!")
        continue
    except EOFError:
        print("end of file character detected, quitting...")
        break
    except ValueError:
        print("***invalid input, please try again***")
        continue 

print( "\nlist of entered integers:", l)
print( "sum of list values:", sum(l) )
