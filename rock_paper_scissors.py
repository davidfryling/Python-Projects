# master

#imported modules

import time
import math
import random

#call methods

def exitGame(): #debugged & works
    print('Exiting game in...')
    time.sleep(1)
    counter = 5
    while counter > 0:
        print(counter)
        time.sleep(1)
        counter = counter - 1
    quit()

def readyCheck(): #debugged & works
    ready = input('Are you ready to get started (yes or no)?: ').lower() #sanitize input
    time.sleep(.5)
    if ready == 'yes':
        print("Great! Let's begin!")
        time.sleep(2)
        return()
    elif ready == 'no':
        print('Sorry to hear that...')
        time.sleep(2)
        print('Maybe you will be ready next time...')
        time.sleep(2)
        exitGame()
    else:
        print('Please enter yes or no.')
        time.sleep(.5)
        readyCheck()

def randomOpponent(): #debugged & works
    listOfOpponents = ['Larry', 'Curly', 'Moe']
    opponentName = random.choice(listOfOpponents)
    print('Your opponent today is ' + opponentName + '!') 
    return()

def playerMoveChoice(playerScore, opponentScore):
    playerMove = input('What object do you choose (rock, paper, or scissor)?: ').lower() #sanitize input
    if playerMove == 'rock' or playerMove == 'paper' or playerMove == 'scissor':
        print('You picked ' + playerMove + '!')
        time.sleep(.5)
        opponentMove(playerScore, opponentScore, playerMove)
    else:
        print('Please rock, paper, or scissor.')
        time.sleep(.5)
        playerMoveChoice(playerScore, opponentScore)

##def opponentMove(playerScore, opponentScore, playerMove):
##    
##def moveCompare(playerScore, opponentScore, playerMove, opponentMove):

#define 

#define 

#define 

#define



#start program here

print('Welcome to Rock, Paper, Scissors!')
time.sleep(1)
playerName = input("What is your name? ")
time.sleep(.5)
print('Hi, ' + playerName + '! Today, we will test your skills against our bots (Larry, Curly, and Moe) and see if you have the skills to best them in this classic game of chance!')
time.sleep(5)
readyCheck() 
randomOpponent() #debugged up to this point
print("Let's get ready to battle!")
time.sleep(2)
print('Rembember, rock beats scissors, scissors beat paper, and paper beats rock! Best 2 out of 3 wins!')  
time.sleep(5)
playerScore = 0
opponentScore = 0
while playerScore < 2 or opponentScore < 2:
    playerMoveChoice(playerScore, opponentScore)
    print("Test Text") 





