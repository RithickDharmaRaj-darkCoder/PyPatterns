start,end = input("Enter the starting and ending numbers : ").split()
div_num =  int(input("Enter the number which divides : "))
print(f"The numbers divisible by {div_num} from '{start}' to '{end}' are :")
for numbers in range(int(start),int(end)):
    if numbers % numbers == 0 and numbers % 2 != 0 and numbers % 3 != 0 and numbers % 5 != 0 or numbers == 2:
        print(numbers)