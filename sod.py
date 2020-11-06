# master

import time
import math
import random

def charHealth(charHP):
    return (charHP / 50) * 100 #5

def goblinHealth(goblinHP):
    return (goblinHP / 25) * 100 

def exitGame():
    print('Exiting game in...')
    time.sleep(1)
    counter = 5
    while counter > 0: #8
        print(counter)
        time.sleep(1)
        counter = counter - 1
    quit()

def TBC():
    print('To be continued...')
    time.sleep(1)
    exitGame()


def start():
    print('Welcome to The Stone of Dalkai! A role playing game!')
    time.sleep(3)
    char = input("Please enter your character's name: ") #2
    time.sleep(.5)
    print('Thank you! You have named your character: ' + char)
    time.sleep(2)
    readyCheck(char)

def readyCheck(char): #12
    ready = input('Are you ready to get started (yes or no)?: ').lower() #13
    time.sleep(.5)
    if ready == 'yes':
        print("Great! Let's begin!")
        time.sleep(2)
        begin(char)
    elif ready == 'no':
        print('Sorry to hear that...')
        time.sleep(2)
        print('Maybe you will be ready next time...')
        time.sleep(2)
        exitGame()
    else:
        print('Please enter yes or no.')
        time.sleep(1)
        readyCheck(char)

def begin(char):
    print('Long ago, in a land far, far away, there lived a young adventurer named ' + char + '.')
    time.sleep(4)
    print('At the request of the great mage, Gorgoff, ' + char + ' was on a quest to retreive the all-powerful Stone of Delkai.')
    time.sleep(5)
    print('Our story begins as our hero starts his journey in the Valley of Fire...')
    time.sleep(4)
    print('Before we see what awaits ' + char + ', we need to first know what is at stake.')
    time.sleep(4)
    print(char + ' is brave, but not invincible. Make sure that the choices you make in the adventures ahead are the correct ones, or our fearless hero may have to end the quest before it is completed.')
    time.sleep(10)
    charHP = 50 #1
    CH = charHealth(charHP) #3
    displayHealth = str(CH)
    print(char + ' begins the journey with ' + displayHealth + '% health.')
    time.sleep(3)
    valleyFireIntro(char, charHP)

def valleyFireIntro(char, charHP):
    print('As ' + char + ' makes way through the Valley of Fire, it became apparent that there was someone else there... something else. Eyes are upon the adventurer.')
    time.sleep(5)
    print('Our hero quickly takes stock of the situation, noting various natrual defense and offensive positions, and which weapons may be needed in each.')
    time.sleep(4)
    print('Then it happens: the enemy makes itself known. Out from a bolder about a hundred yards in front of ' + char + ' stands a menacing looking creature (a goblin), brandishing a small sword.')
    time.sleep(5)
    print('Our hero knows that there are only 2 decent options in this situation:')
    time.sleep(3)
    print('1) take the high ground on the boulder on the right or...')
    time.sleep(2)
    print('2) take an ambush position in the shallow cave to the left.')
    time.sleep(2)
    valleyChoiceCheck(char, charHP)

def valleyChoiceCheck(char, charHP):
    valleyChoiceOne = input('Where should our hero take position (enter boulder or cave)?: ').lower()
    time.sleep(1)
    if valleyChoiceOne == 'boulder':
        print(char + " quickly climbs the boulder and ready's a defense!")
        time.sleep(2)
        position = 'boulder'
        boulder(char, charHP, position)
    elif valleyChoiceOne == 'cave':
        print(char + " swiftly disappears into the cave and ready's an ambush!")
        time.sleep(2)
        position = 'cave'
        cave(char, charHP, position)
    else:
        print('Please enter boulder or cave.')
        time.sleep(1)
        valleyChoiceCheck(char, charHP)

def boulder(char, charHP, position):
    weaponTup = ('sword', 'bow & arrow')
    print("It's time to take up arms and ready for an attack by the goblin.")
    time.sleep(3)
    print(char + ' is carrying two weapons:')
    time.sleep(1)
    for weapon in weaponTup: #11 and 9
        print('A ' + weapon)
        time.sleep(1)
    time.sleep(1)
    chooseWeapon(char, charHP, position)

def cave (char, charHP, position):
    weaponTup = ('sword', 'bow & arrow')
    print("It's time to take up arms and ready for an attack by the goblin.")
    time.sleep(3)
    print(char + ' is carrying two weapons:')
    time.sleep(1)
    for weapon in weaponTup:
        print('A ' + weapon)
        time.sleep(1)
    chooseWeapon(char, charHP, position)

def chooseWeapon(char, charHP, position):
    weaponInHand = input('Which weapon does our warrior take in hand (enter sword or bow)?: ').lower()
    if weaponInHand == 'sword':
        print(char + ' draws the sword!')
        time.sleep(1)
        valleyBattleOne(char, charHP, position, weaponInHand)
    if weaponInHand == 'bow':
        print(char + " ready's a bow and arrow!")
        time.sleep(1)
        valleyBattleOne(char, charHP, position, weaponInHand)
    
def valleyBattleOne(char, charHP, position, weaponInHand):
    print('The goblin races towards the hero, sword in hand, ready to do its worst!')
    time.sleep(4)
    goblinHP = 25
    if weaponInHand == 'sword' and position == 'cave': #6
        print("The warrior is able to meet the goblin's threat head-on and stabs at the wild creature!")
        time.sleep(2)
        goblinHP = goblinHP - 24
        valleyBattleOneEnd(char, charHP, goblinHP)
    elif weaponInHand == 'bow' and position == 'cave':
        print('The warrior has too little space to draw the bow and take aim before the goblin is close enough to slash over and over!')
        time.sleep(4)
        charHP = charHP - 24
        print(char + ' knows that there is little time to turn this battle around and pulls a dagger as a last resort...')
        daggerCounter = random.randint(10,50)
        if daggerCounter > 24:
            print('It is ' + char + "'s lucky day! The warrior's dagger finds its target!")
            time.sleep(2)
            goblinHP = goblinHP - 24
            valleyBattleOneEnd(char, charHP, goblinHP)
        else:
            print('Sadly, our hero does not deal enough damage in desperate use of the dagger and the goblin continues its ferocious attack...')
            time.sleep(3)
            charHP = charHP - 24
            valleyBattleOneEnd(char, charHP, goblinHP)
    elif weaponInHand == 'bow' and position == 'boulder':
        print("The warrior draws the bow, takes aim, and fires upon the charging goblin!")
        time.sleep(2)
        goblinHP = goblinHP - 24
        valleyBattleOneEnd(char, charHP, goblinHP)
    elif weaponInHand == 'sword' and position == 'boulder':
        print('The goblin sees that the warrior has no range weapon in hand and draws its own slingshot to launch an attack!')
        time.sleep(3)
        charHP = charHP - 24
        print(char + ' knows that there is little time to turn this battle around and pulls a dagger, takes aim, and throws...')
        daggerCounter = random.randint(10,50)
        if daggerCounter > 24:
            print('It is ' + char + "'s lucky day! The warrior's dagger finds its target!")
            time.sleep(2)
            goblinHP = goblinHP - 24
            valleyBattleOneEnd(char, charHP, goblinHP)
        else:
            print('Sadly, our hero does not deal enough damage in desperate use of the dagger and the goblin continues its ferocious attack...')
            time.sleep(3)
            charHP = charHP - 24
            valleyBattleOneEnd(char, charHP, goblinHP)

def valleyBattleOneEnd(char, charHP, goblinHP):
    print('The dust of the battle has cleared... how has our hero faired?')
    time.sleep(4)
    CH = charHealth(charHP)
    displayHealth = str(CH)
    print(char + ' now has ' + displayHealth + '% health.')
    time.sleep(3)
    GH = goblinHealth(goblinHP)
    displayHealth = str(GH)
    print('The goblin now has ' + displayHealth + '% health.')
    time.sleep(3)
    if CH > GH:
        print('Our hero has won!')
        time.sleep(2)
        listItem(char, charHP)
    else:
        print('The hero has lost this battle and must retreat to fight another day...')
        time.sleep(2)
        print('Maybe you will choose wisely next time...')
        time.sleep(2)
        exitGame()
    
def listItem(char, charHP):
    print('The adventurer rifles through his enemies satchel to see what items he can find.')
    time.sleep(2)
    goblinSatchel = ['rotten fruit', 'healing potion', 'smoke bomb']
    for item in goblinSatchel: #10
        print(item)
    time.sleep(1)
    takeItem(char, charHP)

def takeItem(char, charHP):
    satchelLoot = input('Which item does our warrior take from the satchel (enter fruit, potion, or bomb)?: ').lower()
    if satchelLoot == 'fruit':
        print(char + ' takes the rotten fruit. Hey, everyone has to eat...')
        time.sleep(1)
        TBC()
    elif satchelLoot == 'potion':
        print(char + " takes the healing potion.")
        time.sleep(1)
        usePotion(char, charHP)
    elif satchelLoot == 'bomb':
        print(char + " takes the smoke bomb.")
        time.sleep(1)
        TBC()
    else:
        print('Please enter fruit, potion, or bomb.')
        time.sleep(1)
        takeItem(char, charHP)
        
def usePotion(char, charHP):
    print('Our hero takes a drink of the healing potion')
    time.sleep(2)
    healFactor = random.randint(12,14) % 5 #5
    charHP = charHP * healFactor
    CH = charHealth(charHP)
    displayHealth = str(CH)
    print(char + ' now has ' + displayHealth + '% health.')
    time.sleep(3)
    TBC()

start()
    
    

    
    
