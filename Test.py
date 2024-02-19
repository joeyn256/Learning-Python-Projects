import random

def game(n4, g4):
    x = 0
    cowbull = [0, 0]
    while x < 4:
        if g4[x] == n4[x]:
            cowbull[0] += 1
            x + 1
        elif g4[x] in n4:
            for n in n4:
                if g4[x] == n:
                    bulls = bulls + 1
            x + 1
    return(cowbull)
print(game('1223','1224'))
