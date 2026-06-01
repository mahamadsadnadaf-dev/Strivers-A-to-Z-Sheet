def inverted_pyramid(rows):
    for i in range(rows,0,-1):
        print(" "*(rows-i)+"* "*i)
num_rows = 5
inverted_pyramid(num_rows)