# Collection of Alphabetic Numbers...

def a():  #23 Letter 'A' ...
    sq = input("Enter one element : ").upper()
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if ((column == 0 or column == 4) and row != 0) or ((row == 0 or row == 3) and (column > 0 and column < 4)):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()

def b():  #24 Letter 'B' ...
    sq = input("Enter one element : ").upper()
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 0) or (column == 4 and (row != 0 and row != 3 and row != 6)) or (
                    (row == 0 or row == 3 or row == 6) and (0 < column and column < 4)):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()

def c():  #25 Letter 'C' ...
    sq = input("Enter one element : ").upper()
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (0 < column and column < 4)):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()

def d():  #26 Letter 'D' ...
    sq = input("Enter one element : ").upper()
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 1) or (column == 4 and (row != 0 and row != 6)) or (
                    (row == 0 or row == 6) and (column != 4 and column != 6)):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()

def e():  #27 Letter 'E' ...
    sq = input("Enter one element : ").upper()
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 0) or ((row == 0 or row == 3 or row == 6) and (0 < column)):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()

def f():  #28 Letter 'F'
    sq = input("Enter one element : ").upper()
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 0) or ((row == 0 or row == 3) and (column > 0)):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()

def g():  #29 Letter 'G'
    sq = input("Enter one element : ").upper()
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 0) or (column == 4 and (row != 1 and row != 2 and row != 3)) or (
                    row == 0 and (0 < column and column < 4)) or (row == 4 and column != 1) or (
                    row == 5 and column == 2) or (row == 6 and (0 < column and column < 3)):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()