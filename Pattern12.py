def pattern(n):
    for i in range(n):
        left = "".join(str(j) for j in range(1,i+1))
        spaces = " "*(2*(n-i))
        right = "".join(str(j) for j in range(i,0,-1))
        print(left+spaces+right)
    print()

pattern(9)

