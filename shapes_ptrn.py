# Shapes Pattern Files...

def pattern0(): #square...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
       # r = int(input("Enter no.of rows : "))
       # c = int(input("Enter no.of columns : "))
        for row in range(5):
            print("     ", end=" ")
            for column in range(5):
                print(sq,end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern1(): #  Left-A L triangle...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(5):
            print("     ", end=" ")
            for column in range(row+1):
                print(sq,end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern15():  # Triangle...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(5):
            print("    ", end="")
            for space in range(5 - row - 1):
                print(" ", end=" ")
            for column in range(row + 1):
                print(sq+"  ", end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern16():  #  Inverted Left-A L triangle...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(5):
            print("    ", end="")
            for column in range(5 - row, 0, -1):
                print(sq + "", end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern17():  # Right-A L Triangle...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(5):
            print("    ", end="")
            for space in range(5 - row - 1):
                print(" ", end=" ")
            for column in range(row + 1):
                print(sq + "", end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern18():  #  Inverted Triangle...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(5):
            print("    ", end="")
            for space in range(row):
                print(" ", end=" ")
            for column in range(5 - row):
                print(sq + "  ", end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern19():  #  Dimond ♦ ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(6):
            print("    ", end="")
            for space in range(6 - row - 1):
                print(" ", end=" ")
            for column in range(row + 1):
                print(sq+"  ", end=" ")
            print()
        for row in range(5):
            print("    ", end="")
            for space in range(row+1):
                print(" ", end=" ")
            for column in range(5-row):
                print(sq+"  ", end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern20():  # ► Right Arrow  ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(6):
            print("     ", end=" ")
            for column in range(row + 1):
                print(sq, end=" ")
            print()
        for row in range(5):
            print("     ", end=" ")
            for column in range(5 - row, 0, -1):
                print(sq + "", end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern21(): # Inverted Right-A L triangle...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(5):
            print("    ", end="")
            for space in range(row):
                print(" ", end=" ")
            for column in range(5 - row):
                print(sq, end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern22(): # Left Arrow...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        for row in range(6):
            print("    ", end="")
            for space in range(6 - row - 1):
                print(" ", end=" ")
            for column in range(row + 1):
                print(sq + "", end=" ")
            print()
        for row in range(5):
            print("    ", end="")
            for space in range(row + 1):
                print(" ", end=" ")
            for column in range(5 - row):
                print(sq, end=" ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern24():  # Even Triangle ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        # r = int(input("Enter no.of rows : "))
        c = 1
        for row in range(5):
            print("    ", end="")
            for space in range(5 - row - 1):
                print(end="   ")
            for column in range(2 * row + 1):
                print(sq, end="  ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def pattern25():  # Inverted odd Triangle...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        print()
        # r = int(input("Enter no.of rows : "))
        c = 0
        s = 9
        for row in range(s):
            print("    ", end="")
            for space in range(9 - s):
                print(end="  ")
            for column in range(9 - c):
                print(sq + " ", end="  ")
            c += 2
            s -= 2
            print()
    else:
        print("Warning! Enter only '1' Character.")