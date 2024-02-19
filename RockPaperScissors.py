Name1 = str(input("Player 1 Name: "))
Name2 = str(input("Player 2 Name: "))

print("\nPlease Use Lower-Case For The Game!\n")
while True:
    str1 = str(input(Name1 + ", Type: rock, paper, or scissors: "))
    str2 = str(input(Name2 + ", Type: rock, paper, or scissors: "))
    if str1 == str2:
        print("Tie! Go Again!\n")
    elif str1 == "rock" and str2 == "scissors":
        print(Name1, "Wins!\n")
        break
    elif str1 == "rock" and str2 == "paper":
        print(Name2, "Wins!\n")
        break
    elif str1 == "paper" and str2 == "rock":
        print(Name1, "Wins!\n")
        break
    elif str1 == "paper" and str2 == "scissors":
        print(Name2, "Wins!\n")
        break
    elif str1 == "scissors" and str2 == "paper":
        print(Name1, "Wins!\n")
        break
    elif str1 == "scissors" and str2 == "rock":
        print(Name2, "Wins!\n")
        break
    else:
        print("Please Use Lowercase... Invalid Game, Try Again!\n")
