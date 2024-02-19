import random
num = random.randint(1,9)
print("\nType 'exit' To End Game\n")
c = 0
while True:
    guess = str(input("Guess Between 1 and 9: "))
    c += 1
    if guess == "exit":
        print("Game Ends")
        break
    elif int(guess) == num:
        print("You Guessed It!!!\nNumber of Tries: ", c)
        break
    elif int(guess) > num:
        print("Over-guess\n")
    else:
        print("Under-guess\n")
        
