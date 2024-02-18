tuple=(1,4,9,16,25,36,49,64,81,100)
X=int(input("enter number to find wether it is available or not"))

while True:
    if (print(X in tuple)):
        print(f"{X} is available")
        break
        
    else:
        print(f"{X} is not availabe")
        break


