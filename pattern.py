# Control of patterns...
from R_tri_ptrn import *
from L_tri_ptrn import *
from shapes_ptrn import *
from alpha_ptrn import  *

def patterns():
    try:
        number = int(input("Enter one number [0-23] : "))
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
            pattern23()
        elif number == 100:
            a()
        elif number == 101:
            b()
        elif number == 102:
            c()
        elif number == 103:
            d()
        elif number == 104:
            e()
        elif number == 105:
            f()
        elif number == 106:
            g()
        elif number == 107:
            h()
        elif number == 108:
            i()
        elif number == 109:
            j()
        elif number == 110:
            k()
        elif number == 111:
            l()
        elif number == 112:
            m()
        elif number == 113:
            n()
        elif number == 114:
            o()
        elif number == 115:
            p()
        elif number == 116:
            q()
        elif number == 117:
            r()
        elif number == 118:
            s()
        elif number == 119:
            t()
        elif number == 120:
            u()
        elif number == 121:
            v()
        elif number == 122:
            w()
        elif number == 123:
            x()
        elif number == 124:
            y()
        elif number == 125:
            z()
        else:
            print("No pattern found!")
    except:
        print("Warning!, enter only numbers.")
        patterns()
patterns()

#Personal Greetings...
print("\nThank You!\n          -darkCoder \U0001F43E")