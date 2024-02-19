import random

def game(n4, g4):
    cowbull = [0, 0]
    x = 0
    for t in range(len(n4)):
        if n4[t] == g4[t]:
            cowbull[0] += 1
        elif g4[t] in n4:
            cowbull[1] += 1
    return(cowbull)

if __name__=="__main__":
    playing = True
    number = str(random.randint(0,9999))
    guesses = 0
    print(number)

    print("Let's play a game of Cowbull!")
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = game(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[0]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
        else:
            print("Your guess isn't quite right, try again.")


                
            
            
            
