# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:25:23 2023

@author: Chintan c shetty
"""

import os.path
import sys
f=input("enter the file name:\n")#input READ.txt
if os.path.isfile(f):
    print("file exists\n")
else:
    print("file doesnt exists")
inf=open(f,'r')
linelist=inf.readlines()
i=0
for line in linelist:
    i+=1
    print(i,':',line)
word=input("enter the word to be counted:\n")
c=0
for i in linelist:
    c+=i.count(word)
print("the word appears ",c,"times")
