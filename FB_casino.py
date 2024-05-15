from random import randint
import time

canplay = 1

def getfirstbucks():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
        if fbs < 10:
           global canplay
           canplay = 0
    file.close()
    
def getfunbucks():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
        if fbs < 10:
           global canplay
           canplay = 0
        print("funbucks balance:", fbs)
    file.close()

def spendfunbucks():
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
    

def smallwin():
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

def bigwin():
    file = open("fb_money.txt", "r") #gets initial value from wallet
    for line1 in file.readlines():
        fbs = (line1)
        fbs = int(fbs)
    file.close()
    
    file = open("fb_money.txt", "w") #converts and writes to the text document 
    fbs = fbs + 80
    fbs = str(fbs)
    file.write(fbs)
    file.close() #wallet update closed

getfirstbucks()  
while canplay == 1:
    getfunbucks()
    time.sleep(0.5)
    gamble = input("would you like to play? ")
    if gamble == "yes":
        time.sleep(0.5)
        spendfunbucks()
        num1 = randint(1,9)
        print(num1)
        time.sleep(0.5)
        num2 = randint(1,9)
        print(num2)
        time.sleep(0.5)
        num3 = randint(1,9)
        print(num3)
        time.sleep(0.5)
        if num1 == num2:
            smallwin()
            if num2 == num3:
                bigwin()
                print("you win 100 funbucks!! :D")
                getfirstbucks()
                time.sleep(0.5)
            else:
                print("you win 20 funbucks :)")
                getfirstbucks()
                time.sleep(0.5)
        elif num2 == num3:
            smallwin()
            print ("you win 20 funbucks :)")
            getfirstbucks()
            time.sleep(0.5)
        elif num1 == num3:
            smallwin()
            print ("you win 20 funbucks :)")
            getfirstbucks()
            time.sleep(0.5)
        else:
            print("you lose :(")
            getfirstbucks()
            time.sleep(0.5)  
    if gamble == "no":
        print("you're boring")
        time.sleep(0.5)
        
print("you're broke, skill issue, go do some maths or something")

