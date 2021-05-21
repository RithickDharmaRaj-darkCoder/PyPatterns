# pattern files...

def pattern0():
    sq = input("Enter one element : ").upper()
   # r = int(input("Enter no.of rows : "))
   # c = int(input("Enter no.of columns : "))
    for row in range(5):
        for column in range(5):
            print(sq,end=" ")
        print()

def pattern1():
    sq = input("Enter one element : ").upper()
    # r = int(input("Enter no.of rows : "))
    for row in range(5):
        for column in range(row+1):
            print(sq,end=" ")
        print()

def pattern2():
    print()