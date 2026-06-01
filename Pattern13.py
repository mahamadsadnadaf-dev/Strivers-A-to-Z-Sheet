n = 5
num = 1
for i in range(n):
    for j in range(i):
        print(f"{num} ",end="")
        num+=1
    print()
