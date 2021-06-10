# Left-angle Triangle pattern files...

def pattern2(): #invert left L triangle...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(5):
            print("     ",end=" ")
            for column in range(5-row):
                print(sq, end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern3():
    # sq = int(input("How many rows needed? : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(row + 1):
            print(column + 1, end=" ")
        print()

def pattern4():
    # sq = int(input("How many rows needed? : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(row, -1, -1):
            print(column + 1, end=" ")
        print()

def pattern5():
    # sq = int(input("How many rows needed? : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(row + 1):
            print(row + 1, end=" ")
        print()

def pattern6():
    # sq = int(input("How many rows needed? : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(row + 1):
            print(5-row, end=" ")
        print()

def pattern7():
    # sq = int(input("How many rows needed? : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(row + 1):
            print(5 - column, end=" ")
        print()

def pattern8():
    # sq = int(input("How many rows needed? : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(row, -1, -1):
            print(5 - column, end=" ")
        print()

def pattern23():
    # sq = int(input("How many rows needed? : "))
    c = 1
    for row in range(5):
        print("     ", end=" ")
        for column in range(1, c + 1):
            print('*', end=" ")
        c += 2
        print()

def pattern27():
    r = 0
    c = 4
    for row in range(5):
        print("    ", end="")
        for column in range(5):
            if (row == r and column == c):
                print("*", end="  ")
                r += 1
                c -= 1
            elif (row == 0 or column == 0):
                print("*", end="  ")
            else:
                print(end="   ")
        print()

def pattern28():
    for row in range(5):
        print("    ", end="")
        for column in range(5):
            if (column == 0 or row == 4):
                print("*", end="  ")
            elif (row == column):
                print("*", end="  ")
            else:
                print(end="   ")
        print()

def pattern29():
    r = 0
    c = 4
    for row in range(5):
        print("    ", end="")
        for column in range(5):
            if (row == r and column == c):
                print("*", end="  ")
                r += 1
                c -= 1
            elif (column == 4 or row == 4):
                print("*", end="  ")
            else:
                print(end="   ")
        print()

def pattern30():
    k = 0
    for row in range(4):
        print("    ", end=" ")
        for column in range(row + 1):
            print(k, end=" ")
            k += 1
        print()

def pattern32():
    str = list(input("Enter your Name : ").upper())
    len_of_str = len(str)
    for row in range(len_of_str):
        print(' ', end=" ")
        for column in range(row + 1):
            print(str[column], end=" ")
        print()
