# Shapes Pattern Files...

def pattern0(): #square...
    sq = input("Enter one element : ").upper()
   # r = int(input("Enter no.of rows : "))
   # c = int(input("Enter no.of columns : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(5):
            print(sq,end=" ")
        print()

def pattern1(): #  Left-A L triangle...
    sq = input("Enter one element : ").upper()
    # r = int(input("Enter no.of rows : "))
    for row in range(5):
        print("     ", end=" ")
        for column in range(row+1):
            print(sq,end=" ")
        print()

def pattern15():  # Triangle...
    sq = input("Enter one element : ").upper()
    # r = int(input("Enter no.of rows : "))
    for row in range(5):
        print("    ", end="")
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(sq+"  ", end=" ")
        print()

def pattern16():  #  Inverted Left-A L triangle...
    sq = input("Enter one element : ").upper()
    # r = int(input("Enter no.of rows : "))
    for row in range(5):
        print("    ", end="")
        for column in range(5 - row, 0, -1):
            print(sq + "", end=" ")
        print()

def pattern17():  # Right-A L Triangle...
    sq = input("Enter one element : ").upper()
    # r = int(input("Enter no.of rows : "))
    for row in range(5):
        print("    ", end="")
        for space in range(5 - row - 1):
            print(" ", end=" ")
        for column in range(row + 1):
            print(sq + "", end=" ")
        print()