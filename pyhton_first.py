n=5
for a in range(n):
    for b in range(a):
        print('*',end="")
print("")       
for x in range(n,0,-1):
    for y in range(x):
        print("*", end="")
print("")