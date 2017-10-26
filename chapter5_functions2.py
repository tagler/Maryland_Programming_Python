def positive(*args,b=0):
    count = 0
    for x in args:
        if x > b:
            count = count + 1
    return count
