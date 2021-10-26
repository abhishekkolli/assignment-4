#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:36:44 2021

@author: kolliabhishek
"""

"""new program to test if my stats is correct or not"""
import statistics
f = open("numbers.txt","r")
string=f.read()
f.close()
arraynum = string.split()
j=0
for i in arraynum:
    #numarray.append(int(i))
    arraynum[j] = int(i)
    j+=1
#print(arraynum)
print("mean: ",statistics.mean(arraynum))
print("median: ",statistics.median(arraynum))
print("mode: ",statistics.mode(arraynum))
print("variance: ",round(statistics.variance(arraynum),2))
print("standard deviation: ",round(statistics.stdev(arraynum),2))

"My program is correct but the median in my calculation slightly differs for even because" 
"the stats module gives mid value of an array after sorting the list"
"""
My program values
mean:  51.8
median:  54.5
mode:  91
variance:  833.192
standard deviation:  28.87"""

"""Statistics module values on the same data set
mean:  51.8
median:  54.0
mode:  91
variance:  833.19
standard deviation:  28.87"""
