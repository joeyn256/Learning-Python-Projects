import random

def weak():
    list1 = ['deserve', 'graceful', 'field', 'ear', 'silk', 'ossified', 'solid',
            'terrible', 'record', 'room', 'fabulous', 'sprout', 'cat', 'release',
            'geese', 'flock', 'lock', 'tiger', 'next', 'bait', 'clip', 'rest',
            'test', 'example', 'basket']
    return list1[random.randint(0,24)]

def medium():
    password = weak() + "_" + weak()
    randnum = random.randint(0, len(password) - 1)
    count = 0
    newpassword = ""
    while (randnum == password.index('_')):
        randnum = random.randint(0, len(password) - 1)
    for a in password:
        if count == randnum:
            newpassword += a.upper()
            count += 1
        else:
            newpassword += a
            count += 1
    return newpassword

def strong():
    password = medium() + "_" + medium()
    randnum = random.randint(0,9)
    password1 = ""
    count1 = 0
    randind1 = random.randint(0,len(password) - 1)
    while (password[randind1] == '_'):
        randind1 = random.randint(0,len(password) - 1)
    for a in password:
        if count1 == randind1:
            password1 += str(randnum)
            password1 += a
            count1 += 1
        else:
            password1 += a
            count1 += 1
    char = "!@#$%^&*~`"
    count2 = 0
    randchar = char[random.randint(0, len(char) - 1)]
    randind2 = random.randint(0,len(password1) - 1)
    password2 = ""
    while (password[randind2] == '_'):
        randind2 = random.randint(0,len(password1) - 1)
    for a in password1:
        if count2 == randind2:
            password2 += randchar
            password2 += a
            count2 += 1
        else:
            password2 += a
            count2 += 1

    return password2
    
    

    
while True:
    print("Valid Password Strengths: 'weak', 'medium', 'strong'\n")
    strength = input("Type strength of password: ")
    if strength == "weak":
        print("Password: " + weak())
        break
    elif strength == "medium":
        print("Password: " + medium())
        break
    elif strength == "strong":
        print("Password: " + strong())
        break
    else:
        print("Invalid Strenth Typed, Please Type Again!")
