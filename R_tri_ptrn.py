# Right-angle Triangle pattern files...

def pattern9():
    # sq = int(input("How many rows needed? : "))
    for row in range(5):
        print("     ", end=" ")
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(column + 1, end=" ")
        print()

def pattern10():
    for row in range(5):
        print("     ", end=" ")
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(row + 1 - column, end=" ")
        print()

def pattern11():
    for row in range(5):
        print("     ", end=" ")
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(row + 1, end=" ")
        print()

def pattern12():
    for row in range(5):
        print("     ", end=" ")
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(5 - row, end=" ")
        print()

def pattern13():
    for row in range(5):
        print("     ", end=" ")
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(5 - column, end=" ")
        print()

def pattern14():
    for row in range(5):
        print("     ", end=" ")
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row, -1, -1):
            print(5 - column, end=" ")
        print()

def pattern26():
    for row in range(5):
        print("    ", end="")
        for column in range(5):
            if (column == 4) or (row == 0):
                print("*", end="  ")
            elif (row == column):
                print("*", end="  ")
            else:
                print(end="   ")
        print()

def pattern31():
    k = 0
    for row in range(4):
        print("    ", end=" ")
        for space in range(4 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(k, end=" ")
            k += 1
        print()

def pattern33():
    str = list(input("Enter your Name : ").upper())
    len_of_str = len(str)
    for row in range(len_of_str):
        print(' ', end=" ")
        for space in range(len_of_str - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(str[column], end=" ")
        print()