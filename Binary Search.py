def Binary(list1, a1):
    for x in list1:
        if x == a1:
            print('Number in inside the list')
        else:
            print('Number is not inside the list')

x1 = Binary([1,2,3,4,5,6,7], 5)
print(x1)
x2 = Binary([1,2,3,4,5,6,7], 8)
print(x2)
    
