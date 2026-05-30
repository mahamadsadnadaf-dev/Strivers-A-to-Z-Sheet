def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print leading spaces, then print the stars separated by spaces
        print(" " * (rows - i) + "* " * i)

# Change this number to make the pyramid larger or smaller
num_rows = int(input("Enter no of rows : "))
inverted_pyramid(num_rows)