#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:09:36 2021

@author: kolliabhishek
"""

"""recursive valid email"""
def validemail(email,i=0):
    if i==len(email):
        return print("did not find @")
    if email[i]=="@":
        return print("found @ at index",i)
    else:
        return validemail(email,i+1)

test1="test@gmail.com"
test2="charliebrown@gmail.com"
test3="testgmail.com"
validemail(test3)
