l1 = ["A","B","C","D","E"]
for i in range(len(l1),0,-1):
    for j in range(i):
        print(l1[j],end="")
    print()