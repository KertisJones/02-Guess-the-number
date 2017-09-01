#!/usr/bin/env python3

import sys
import random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

ranNum = random.randint(0, 100)
guessNum = -1
guessRemaining = 5
stillPlaying = True


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

    
while (stillPlaying):
    print("Guess the number that I'm thinking of from 0 to 100. You have 5 tries.")
    print("")
    while (guessRemaining > 0):
        guessNum = input("~ ")
        if (RepresentsInt(guessNum)):
            guessNum = int(guessNum)
            if(guessNum == ranNum):
                print("You Got it! " + str(guessNum) + " is the answer!")
                print("")
                guessRemaining = 0
            else:
                if(guessNum == 69):            
                    print("Seriously?")
                if(guessNum > ranNum):            
                    print("Not quite, " + str(guessNum) + " is too high.")
                elif(guessNum < ranNum):
                    print("Not quite, " + str(guessNum) + " is too low.")
                else:
                    print("You're not supposed to see this...")
                    print("")
                    guessRemaining = 0
                guessRemaining = guessRemaining - 1
                if (guessRemaining != 1):
                    print("You have " + str(guessRemaining) + " tries remaining.")
                else:
                    print("You have " + str(guessRemaining) + " try remaining.")
                print("")
        else:
            print("Oops! " + guessNum + " is not a number! Try again.")
    if(guessNum == ranNum):
        print("YOU WIN!")
        print("")
        print("The number was " + str(ranNum) + "!")
        guessRemaining = 0
    else:
        print("GAME OVER")
        print("")
        print("The number was " + str(ranNum) + ".")
    if(ranNum == 69):            
        print("lol")
    print("")
    print("--------------------------------------------------")
    playAgain = input("PLAY AGAIN? (y/n) ").lower()
    if("y" in playAgain):
        ranNum = random.randint(0, 100)
        guessRemaining = 5
        stillPlaying = True
    else:
        stillPlaying = False
    print("--------------------------------------------------")
    print("")
