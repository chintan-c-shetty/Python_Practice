# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:44:00 2023

@author: Chintan c shetty
"""

import re
def withoutregx(phnum):
    if (len(phnum))!=12:
        return False
    for i in range(len(phnum)):
        if i==3 or i==7 :
            if phnum[i]!='-':
               return False
        else:
            if phnum[i].isdigit()==False:
                return False
    return True
def withregx(phnum):
    pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pattern.match(phnum):
        return True     
    else:
        return False
n=input("enter the phone number:\n")
print("without regular expression")
if withoutregx(n):
    print("the phone number is valid")
else:
    print("phone number is invalid")
print("with regular expression")
if withregx(n):
    print("the phone number is valid")
        