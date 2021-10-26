#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 01:16:12 2021

@author: kolliabhishek
"""
"""I need help on this question please make some comments so I can proceed on the input parsing to path"""
import os
input1=input("enter directoryname: ")
#print(os.walk("."))
for dirpath, dirs, files in os.walk("/Users/kolliabhishek/Downloads/assignment 4"):	 
	path = dirpath.split('/')
	print ((len(path))*'--', '[',os.path.basename(dirpath),']')
	for f in files:
		print (len(path)*'--', f)