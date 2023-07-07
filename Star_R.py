def print_star_R(rows):
    for i in range(rows):
        for j in range(rows):
            if j == 0 or (j == rows-1 and (i != 0 and i != rows//2)) or (i == 0 or i == rows//2) and j != 0 and j != rows-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example usage:
print_star_R(5)
