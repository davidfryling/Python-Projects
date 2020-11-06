# master

#imports

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
        time.sleep(2)
        readyCheck()

#define 

#define 

#define 

#define



#start program here

print('Welcome to Rock, Paper, Scissors!')
time.sleep(2)
print('Instructions...')
time.sleep(7)
playerName = input("What is your name? ")
time.sleep(.5)
print('Thank you, ' + playerName + '!')
time.sleep(2)
readyCheck()
print("Test Return") #debugged up to this point



