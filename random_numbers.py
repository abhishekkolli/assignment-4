#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:42:52 2021

@author: kolliabhishek
"""

"""creating a module random numbers"""
import random
def generate(count,Flag = False):
    array=[]
    for i in range(count):
        array.append(random.randrange(0,100))
        i+=1
    array = sorted(array)
    if Flag == True:
        f = open("numbers.txt",'w')
        for i in array:
            f.write(str(i)+"\n")
        f.close()
    return sorted(array)

if __name__=="__main__":
    print(generate(100,True))
        
    
    
    