#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:30:15 2021

@author: kolliabhishek
"""

import random
def hangman(computerchoice,guesses):
    chars=[]
    while guesses>0:
        userinput = input("Guess a letter?")
        guesses = guesses - 1
        if userinput in computerchoice:
            print(userinput,"is in the word:",end="")
            chars.append(userinput)
            for char in computerchoice:
                if char in chars:
                    print(char,end="")
                else:
                    print("_ ",end="")
            userguess = input("Try and guess the word?")
            if userguess.lower() == computerchoice:
                print("Congratulations!")
                print("The word was",computerchoice)
                return
            
            else:
                print("That is not the word")
                continue
        else:
            print(userinput," is not in the word")
            print("You have {} guesses remaining".format(guesses))
    if guesses == 0:
        print("You ran out of guesses, the word is:",computerchoice)

if __name__=="__main__":
    f=open("common_words.txt","r")
    entirefile=f.read()
    f.close()
    common_words=entirefile.split()
#print(common_array)
    play="y"
    guesses=5
    while play=="y":
        computerchoice=random.choice(common_words)
        hangman(computerchoice,guesses)
        play = input("would you like to play again?")
        guesses = 5
