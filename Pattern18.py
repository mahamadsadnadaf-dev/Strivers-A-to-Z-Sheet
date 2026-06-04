import string

l = list(string.ascii_uppercase)

k = 0
for row in range(1, 4):
    for _ in range(row):
        print(l[k], end="")
        k += 1
    print()