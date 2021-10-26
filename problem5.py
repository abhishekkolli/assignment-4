#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:12:08 2021

@author: kolliabhishek
"""

import random_numbers
#print(random_numbers.generate(17,False))
from math import sqrt
def stats(count=100):
    array = random_numbers.generate(count,True)
    Total = sum(array)
    mean = Total/count
    if count%2 == 0:
        medianindex = count//2
        median = (array[medianindex]+array[medianindex+1])/2
    else:
        medianindex = count//2+1
        median = array[medianindex]
    arraydict={}
    for i in array:
        arraydict[i] = arraydict.get(i,0)+1
    maxfrequency = max(arraydict.values())
    #print(maxfrequency)
    for i in array:
        #print(i, arraydict[i])
        if arraydict[i] == maxfrequency:
            mode = i
            break
    variance_num=0
    for i in array:
        variance_num= variance_num + (i-mean)**2
    
    variance = variance_num/(count-1)
    standard_deviation = sqrt(variance)
    return mean, median, mode, round(variance,3), round(standard_deviation,2)

if __name__== "__main__":
    #print(stats(25))
    input1=input("enter number: ")
    try :
        int(input1)
        a,b,c,d,e = stats(int(input1))
        print("mean: ",a)
        print("median: ",b)
        print("mode: ",c)
        print("variance: ", d)
        print("standard deviation: ", e)
    except ValueError:
        print("enter a valid number")
        
    