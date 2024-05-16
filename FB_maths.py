import random

ans = 0
play = 1
guess = 0

instructions()

def winfbeasy():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
    file.close()
            
    file = open("fb_money.txt", "w") #converts and writes to the text document 
    fbs = fbs + 10
    fbs = str(fbs)
    file.write(fbs)
    file.close() #wallet update closed

def winfbmedium():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
    file.close()
            
    file = open("fb_money.txt", "w") #converts and writes to the text document 
    fbs = fbs + 20
    fbs = str(fbs)
    file.write(fbs)
    file.close() #wallet update closed

def winfbhard():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
    file.close()
            
    file = open("fb_money.txt", "w") #converts and writes to the text document 
    fbs = fbs + 30
    fbs = str(fbs)
    file.write(fbs)
    file.close() #wallet update closed

def loosefbeasy():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
    file.close()
            
    file = open("fb_money.txt", "w") #converts and writes to the text document 
    fbs = fbs - 2
    fbs = str(fbs)
    file.write(fbs)
    file.close() #wallet update closed

def loosefbmedium():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
    file.close()
            
    file = open("fb_money.txt", "w") #converts and writes to the text document 
    fbs = fbs - 5
    fbs = str(fbs)
    file.write(fbs)
    file.close() #wallet update closed

def loosefbhard():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
    file.close()
            
    file = open("fb_money.txt", "w") #converts and writes to the text document 
    fbs = fbs - 10
    fbs = str(fbs)
    file.write(fbs)
    file.close() #wallet update closed

def instructions(): 
    print("guess the answer right to win (-1 = menu) ")

def gameplay():
    mode = input("enter mode, hard/medium/easy: ")
    if mode == "hard":
        while play == 1:
            newproblemhard()
            checkscorehard()
    elif mode == "medium":
        while play == 1:
            newproblemmedium()
            checkscoremedium()
    elif mode == "easy":
        while play == 1:
            newproblemeasy()
            checkscoreasy()

def newproblemhard():
    global guess
    global ans
    FN = random.randint(6,20)
    SN = random.randint(6,20)
    ans = FN * SN
    guess = input(f"{FN} * {SN} = ")
    guess = (int(guess))

def newproblemmedium():
    global guess
    global ans
    FN = random.randint(3,12)
    SN = random.randint(3,12)
    ans = FN * SN
    guess = input(f"{FN} * {SN} = ")
    guess = (int(guess))

def newproblemeasy():
    global guess
    global ans
    FN = random.randint(1,5)
    SN = random.randint(1,5)
    ans = FN * SN
    guess = input(f"{FN} * {SN} = ")
    guess = (int(guess))

def checkscoreasy():
    global guess
    global ans
    if guess == ans:
        print(f"you got it right the answer was:{ans}: you have had 10 funbucks added to your wallet")
        winfbeasy()
    elif guess == -1:
        global play
        play = 0
        menu()
    elif guess != ans:
        print(f"your answer was incorrect, the correct answer is:{ans}: 2 funbucks deducted")
        loosefbeasy()
    

def checkscoremedium():
    global guess
    global ans
    if guess == ans:
        print(f"you got it right the answer was:{ans}: you have had 20 funbucks added to your wallet")
        winfbmedium()
    elif guess == -1:
        global play
        play = 0
        menu()
    elif guess != ans:
        print(f"your answer was incorrect, the correct answer is:{ans}: 5 funbucks deducted")
        loosefbmedium()
    

def checkscorehard():
    global guess
    global ans
    if guess == ans:
        print(f"you got it right the answer was:{ans}: you have had 30 funbucks added to your wallet")
        winfbhard()
    elif guess == -1:
        global play
        play = 0
        menu()
    elif guess != ans:
        print(f"your answer was incorrect, the correct answer is:{ans}: 10 funbucks deducted")
        loosefbhard()
    

def menu():
    print("-1 to quit game")
    gameplay()

    
if play == 1:
    gameplay()
else:
    pass
    



