# pattern files...

def pattern0(): #square...
    sq = input("Enter one element : ").upper()
   # r = int(input("Enter no.of rows : "))
   # c = int(input("Enter no.of columns : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(5):
            print(sq,end=" ")
        print()

def pattern1(): #left L triangle...
    sq = input("Enter one element : ").upper()
    # r = int(input("Enter no.of rows : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(row+1):
            print(sq,end=" ")
        print()

def pattern2(): #invert left L triangle...
    sq = input("Enter one element : ").upper()
    # r = int(input("Enter no.of rows : "))
    for row in range(5):
        print("     ",end=" ")
        for column in range(5-row):
            print(sq, end=" ")
        print()

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