num = int(input("Enter Number: "))
x = range(2, num - 1)
a = []
for elem in x:
    if num % elem == 0:
        a.append(elem)
print(a)
        
