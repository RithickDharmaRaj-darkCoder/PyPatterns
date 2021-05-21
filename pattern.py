# Control of patterns...
from ptrn_lst import *

number = int(input("Enter one number [0-N] : "))

if number == 0:
    pattern0()
elif number == 1:
    pattern1()
else:
    print("No pattern found!")