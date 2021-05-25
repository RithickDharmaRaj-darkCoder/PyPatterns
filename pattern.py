# Control of patterns...
from R_tri_ptrn import *
from L_tri_ptrn import *

def patterns():
    try:
        number = int(input("Enter one number [0-12] : "))

        if number == 0:
            pattern0()
        elif number == 1:
            pattern1()
        elif number == 2:
            pattern2()
        elif number == 3:
            pattern3()
        elif number == 4:
            pattern4()
        elif number == 5:
            pattern5()
        elif number == 6:
            pattern6()
        elif number == 7:
            pattern7()
        elif number == 8:
            pattern8()
        elif number == 9:
            pattern9()
        elif number == 10:
            pattern10()
        elif number == 11:
            pattern11()
        elif number == 12:
            pattern12()
        else:
            print("No pattern found!")
    except:
        print("Warning!, enter only numbers.")
        patterns()
patterns()

#Personal Greetings...
print("\nThank You!\n          -darkCoder \U0001F43E")