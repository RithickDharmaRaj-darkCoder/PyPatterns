# Control of patterns...
from R_tri_ptrn import *
from L_tri_ptrn import *
from shapes_ptrn import *
from alpha_ptrn import  *

def patterns():
    try:
        number = int(input("Enter one number [0-48] : "))
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
        elif number == 13:
            pattern13()
        elif number == 14:
            pattern14()
        elif number == 15:
            pattern15()
        elif number == 16:
            pattern16()
        elif number == 17:
            pattern17()
        elif number == 18:
            pattern18()
        elif number == 19:
            pattern19()
        elif number == 20:
            pattern20()
        elif number == 21:
            pattern21()
        elif number == 22:
            pattern22()
        elif number == 23:
            a()
        elif number == 24:
            b()
        elif number == 25:
            c()
        elif number == 26:
            d()
        elif number == 27:
            e()
        elif number == 28:
            f()
        elif number == 29:
            g()
        elif number == 30:
            h()
        elif number == 31:
            i()
        elif number == 32:
            j()
        elif number == 33:
            k()
        elif number == 34:
            l()
        elif number == 35:
            m()
        elif number == 36:
            n()
        elif number == 37:
            o()
        elif number == 38:
            p()
        elif number == 39:
            q()
        elif number == 40:
            r()
        elif number == 41:
            s()
        elif number == 42:
            t()
        elif number == 43:
            u()
        elif number == 44:
            v()
        elif number == 45:
            w()
        elif number == 46:
            x()
        elif number == 47:
            y()
        elif number == 48:
            z()
        else:
            print("No pattern found!")
    except:
        print("Warning!, enter only numbers.")
        patterns()
patterns()

#Personal Greetings...
print("\nThank You!\n          -darkCoder \U0001F43E")