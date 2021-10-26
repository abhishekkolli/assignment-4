#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:34:28 2021

@author: kolliabhishek
"""

"""new program to find GCD"""
def greatest_common_divisor(a,b):
    if b==0:
        return a
    else:
        remainder = a%b
        return greatest_common_divisor(b, remainder)
a=128
b=64
print(greatest_common_divisor(a, b))