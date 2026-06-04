l = ["A","B","C","D","E"]
for i in range(len(l)):
    for j in range(i + 1):
        print(l[i], end="")
    print()