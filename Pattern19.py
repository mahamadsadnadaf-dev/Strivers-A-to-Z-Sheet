# Number of rows in each half
n = 5
for i in range(n):
    # Calculate stars and spaces
    stars = n - i
    spaces = 2 * i
    
    # Print left stars + middle spaces + right stars
    print("*" * stars + " " * spaces + "*" * stars)

for i in range(n):
    # Calculate stars and spaces
    stars = i + 1
    spaces = (n * 2) - (2 * stars)
    
    # Print left stars + middle spaces + right stars
    print("*" * stars + " " * spaces + "*" * stars)