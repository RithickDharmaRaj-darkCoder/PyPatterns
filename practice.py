# Printing Prime Numbers...
print("    *** Printing Prime Numbers ***")
start,end = input("Enter the starting and ending numbers : ").split()
print(f"The Prime Numbers from {start} to {end} are : ")
for numbers in range(int(start),int(end) + 1):
    if numbers % numbers == 0 and numbers % 2 != 0 and numbers % 3 != 0 and numbers % 5 != 0 or numbers == 2 or numbers == 3 or numbers == 5:
        if numbers == 1:
            continue
        print(numbers)

#Personal Greetings...
print("Thank You!","\n","          -darkCoder \U0001F43E")