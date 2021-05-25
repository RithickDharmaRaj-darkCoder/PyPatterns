# Right-angle Triangle pattern files...

def pattern9():
    # sq = int(input("How many rows needed? : "))
    for row in range(5):
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(column + 1, end=" ")
        print()