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