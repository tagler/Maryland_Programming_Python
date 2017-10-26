for x in range(0,50,1):
    if x == 0:
        print("  ",x,sep="",end="\t")
    elif x % 10 != 0:
        print(x,end="\t")
    else:
        print("\n",x,end="\t")
    
