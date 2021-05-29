# Collection of Alphabetic Numbers...

def a():  #23 Letter 'A' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if ((column == 0 or column == 4) and row != 0) or ((row == 0 or row == 3) and (column > 0 and column < 4)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def b():  #24 Letter 'B' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or (column == 4 and (row != 0 and row != 3 and row != 6)) or (
                        (row == 0 or row == 3 or row == 6) and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def c():  #25 Letter 'C' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def d():  #26 Letter 'D' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 1) or (column == 4 and (row != 0 and row != 6)) or (
                        (row == 0 or row == 6) and (column != 4 and column != 6)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def e():  #27 Letter 'E' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or ((row == 0 or row == 3 or row == 6) and (0 < column)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def f():  #28 Letter 'F' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or ((row == 0 or row == 3) and (column > 0)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def g():  #29 Letter 'G' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
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
    else:
        print("Warning! Enter only '1' Character.")

def h():  #30 Letter 'H' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0 or column == 4) or (row == 3):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def i():  #31 Letter 'I' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 2) or (row == 0 or row == 6):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def j():  #32 Letter 'J' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 2) or (row == 0) or (row == 6 and column < 2) or (column == 0 and row == 5):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def k():  #33 Letter 'K' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        r = 0
        c = 4
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0):
                    print(f" {sq} ", end="")
                elif (row == column + 2 and column > 1):
                    print(f" {sq} ", end="")
                elif (row == r and column == c):
                    print(f" {sq} ", end="")
                    r += 1
                    c -= 1
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def l():  #34 Letter 'L' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        r = 0
        c = 4
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or (row == 6):
                    print(f" {sq} ",end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

