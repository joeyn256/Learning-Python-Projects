import random

a1 = [random.randint(1,20) for x in range(20)]

def Remove1(l1):
    a1 = []
    for x in l1:
        if x not in a1:
            a1.append(x)
    return a1

def Remove2(x):
    x = set(x)
    x = list(x)
    return x

print(Remove1(a1))
print(Remove2(a1))
a1.sort() #test
print(a1) #test


