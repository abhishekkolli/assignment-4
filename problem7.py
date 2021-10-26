#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:20:50 2021

@author: kolliabhishek
"""

"""change rock paper scissors program"""
import random
#initiate the play to yes so the program runs for the first time

def game(userinput):
    computerobject= random.choice(["rock","paper","scissors"])
    winset=('rock-scissors','scissors-paper','paper-rock')
    if userinput not in ["rock","paper","scissors"]:
        print("You must choose rock, paper or scissors")
        return 1
    else:
        comparison=userinput+'-'+computerobject
        print(comparison)
        if comparison in winset:
            print("The computer choose ",computerobject," ","you win!")
            return 1
        elif userinput == computerobject:
            print("The computer choose ",computerobject," ","Let's settle this")
            return None
            #incase if the game is a tie then you have to play again hence the use of continue 
        else:
            print("The computer choose",computerobject," ","the computer wins")
            return 1



if __name__=="__main__":
    play='y'
    while play=='y':
#converting the input to lower case just incase if the user makes a wrong entry
        userinput = input("Choose:").lower()
        value = game(userinput)
        if value is None:
            continue
        play = input("Would you like to play again?")
        
        