x, y, z, n = map(int, input().split())
if(n<x and n<y and n<z):
    if(x<y and x<z):
        print("L1")
    elif(y<x and y<z):
        print("L2")
    else:
        print("L3")
elif(n<x and n<y):
    if(x<y):
        print("L1")
    else:
        print("L2")
elif(n<y and n<z):
    if(y<z):
        print("L2")
    else:
        print("L3")
elif(n<x and n<z):
    if(x<z):
        print("L1")
    else:
        print("L3")
elif(n<x):
    print("L1")
elif(n<y):
    print("L2")
elif(n<z):
    print("L3")
else:
    print("0")

