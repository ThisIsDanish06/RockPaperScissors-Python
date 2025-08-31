# Write a code to make Rock, Paper, and Scissor game

import random

computer = random.choice([1,-1,0])
Youstr = input("Enter your choice: ")
YouDict = {"r" : 1, "p" : -1, "s" : 0}
ReverseDict = {1 : "Rock", -1 : "Paper", 0 : "Scissor"}

You = YouDict[Youstr]

# From now on, we only have two variables which are You and Computer

print(f"You chose {ReverseDict[You]}!\nComputer chose {ReverseDict[computer]}!")

if(computer==You):
    print("It's a draw!")
else:
    if(computer == 1 and You == -1):
        print("You Win!")

    elif(computer == 1 and You == 0):
        print("You Lose!")

    if(computer == -1 and You == 1):
        print("You Lose!")

    elif(computer == -1 and You == 0):
        print("You Win!")

    elif(computer == 0 and You == 1):
        print("You Win!")

    elif(computer == 0 and You == -1):
        print("You Lose!")




