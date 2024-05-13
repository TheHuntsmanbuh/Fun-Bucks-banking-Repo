import random

ans = 0
play = 1
guess = 0
def instructions(): 
    print("guess the answer right to win (-1 = menu) ")

def gameplay():
    mode = input("enter mode, hard/medium/easy:")
    if mode == "hard":
        while play == 1:
            newproblemhard()
            checkscore()
    elif mode == "medium":
        while play == 1:
            newproblemmedium()
            checkscore()
    elif mode == "easy":
        while play == 1:
            newproblemeasy()
            checkscore()

def newproblemhard():
    global guess
    global ans
    FN = random.randint(1,12)
    SN = random.randint(1,12)
    ans = FN * SN
    guess = input(f"{FN} * {SN} =")
    guess = (int(guess))

def newproblemmedium():
    global guess
    global ans
    FN = random.randint(1,7)
    SN = random.randint(1,7)
    ans = FN * SN
    guess = input(f"{FN} * {SN} =")
    guess = (int(guess))

def newproblemeasy():
    global guess
    global ans
    FN = random.randint(1,5)
    SN = random.randint(1,5)
    ans = FN * SN
    guess = input(f"{FN} * {SN} =")
    guess = (int(guess))

def checkscore():
    global guess
    global ans
    if guess == ans:
        print(f"you got it right the answer was:{ans}: you have had 10 funbucks added to your wallet")
    elif guess != ans:
        print(f"your answer was incorrect, the correct answer is:{ans}: 2 funbucks deducted")
    elif guess == -1:
        global play
        play = 0
        menu()

def menu():
    print("-1 to quit game")

gameplay()

    
if play == 1:
    gameplay()
else:
    pass
    

