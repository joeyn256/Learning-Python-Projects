import random

a = [random.randint(1,100) for x in range(1,random.randint(1,20))]
b = random.sample(range(100), random.randint(1,20))
a.sort()
b.sort()
print(a)
print(b)

c = [d for d in set(a) if d in b]
result = []
for element in c:
    if element not in result:
        result.append(element)
print(c)
