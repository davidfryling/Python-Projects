# master branch

#imported modules

import time
import math
import random

##def readyCheck(): #not necessary
##    ready = input('Are you ready to get started (yes or no)?: ').lower() #sanitize input
##    time.sleep(.5)
##    if ready == 'yes':
##        print("Great! Let's begin!")
##        time.sleep(1)
##        main()
##    elif ready == 'no':
##        print('Sorry to hear that...')
##        time.sleep(1)
##        print('Maybe next time...')
##        time.sleep(1)
##        exitGame()
##    else:
##        print('Please enter yes or no.')
##        time.sleep(.5)
##        readyCheck()

#call functions

def exitGame(): #allows game to end after each match
    print('Exiting game in...')
    time.sleep(1)
    counter = 5
    while counter > 0:
        print(counter)
        time.sleep(1)
        counter = counter - 1
    quit()

def playerMoveChoice(): #creates and stores usable player move to play in each while loop
    global playerMove
    playerMove = input('What object do you choose (rock, paper, or scissor)?: ').lower() #sanitize input
    if playerMove == 'rock' or playerMove == 'paper' or playerMove == 'scissor':
       return(playerMove)
    else:
        print('Please enter rock, paper, or scissor.') 
        time.sleep(.5)
        playerMoveChoice()

def playAgainChoice(): #allows player to continue or leave the game
    playAgain = input('Would you like to play again (yes or no)?: ').lower() #sanitize input
    if playAgain == 'yes':
        print("Great! Let's start over!")
        time.sleep(1)
        main()
    elif playAgain == 'no':
        print('Sorry to hear that...')
        time.sleep(1)
        print('Maybe next time...')
        time.sleep(1)
        exitGame()
    else:
        print('Please enter yes or no.')
        time.sleep(.5)
        playAgainChoice()

#intro (only runs the first time through in order to welcome player and get their name)

def intro(): #bug free
    print('Welcome to Rock, Paper, Scissors!')
    time.sleep(1)
    global playerName
    playerName = input("What is your name? ")
    time.sleep(.5)
    print('Hi, ' + playerName + '! Today, you will test your skills against one of our bots (Larry, Curly, or Moe) and see if you have the skills to best them in this classic game of chance!')
    time.sleep(3)
    main() 

#main program here, which can be rerun until the play chooses not to continue

def main(): 
    listOfOpponents = ['Larry', 'Curly', 'Moe']
    opponentName = random.choice(listOfOpponents)
    print('This time, your opponent is ' + opponentName + '!')
    time.sleep(2)
    print("Get ready to battle!")
    time.sleep(1)
    print('Rembember, rock beats scissors, scissors beat paper, and paper beats rock! Best 2 out of 3 wins!')  
    time.sleep(3) 
    playerScore = 0
    opponentScore = 0
    roundCounter = 1
    while playerScore < 2 and opponentScore < 2:
        print('Round ' + str(roundCounter) + '!')
        time.sleep(1)
        playerMoveChoice()
        print('You picked ' + playerMove + '...')
        time.sleep(1)
        moveList = ['rock', 'paper', 'scissor']
        opponentMove = random.choice(moveList)
        print(opponentName + ' picked ' + opponentMove + '...')
        time.sleep(1)
        if playerMove == opponentMove:
            print('You both picked the same thing, no points for either of you...')
            time.sleep(2)
            playerScore = playerScore + 0 #is this necessary?
            opponentScore = opponentScore + 0 #is this necessary?
        elif playerMove == 'rock' and opponentMove == 'paper' or playerMove == 'paper' and opponentMove == 'scissor' or playerMove == 'scissor' and opponentMove == 'rock':
            print('Unfortunately, ' + opponentMove + ' beats ' + playerMove + ', so ' + opponentName + ' wins this round and gets a point...')
            time.sleep(2)
            playerScore = playerScore + 0
            opponentScore = opponentScore + 1 
        else:
            print('Nice job, ' + playerName + ', ' + playerMove + ' beats ' + opponentMove + ', so you win this round and get a point!')
            time.sleep(2)
            playerScore = playerScore + 1 
            opponentScore = opponentScore + 0 
        print("Let's check the score...")
        time.sleep(1)
        print('Your score is ' + str(playerScore))
        time.sleep(1)
        print(opponentName + "'s score is " + str(opponentScore))
        time.sleep(1)
        roundCounter = roundCounter + 1
    print("Drumroll please...")
    time.sleep(2)
    if playerScore > opponentScore:
        print('Congrats, ' + playerName + '! You won!')
        time.sleep(1)
    else:
        print('Sorry, ' + playerName + ', but ' + opponentName + ' won this time... Maybe you will have better luck next time...')
        time.sleep(3)
    playAgainChoice()

#initiate start of game (i.e., intro program)
intro()



