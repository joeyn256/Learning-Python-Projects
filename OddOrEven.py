num = int(input("First Number: "))
if num % 4 == 0:
    print(num, "is divisible by 4")
elif num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
check = int(input("Divisible by: "))
if num % check == 0:
    print("Yes")
else:
    print("No")
            
