a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
hold = 0
for x in a:
    if x == hold:
        continue
    elif x in b:
        c.append(x)
        hold = x
print(c)
        
