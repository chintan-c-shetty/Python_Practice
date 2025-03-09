# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:10:58 2023

@author: Chintan c shetty
"""

import sys
def romtodec(roman):
    romandict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    last="I"
    num=0
    for i in roman:
        if i  not in romandict:
            print("invalid input")
            sys.exit(0)
    for j in roman[::-1]:
        if romandict[j] < romandict[last]:
            num-=romandict[j]
        else:
            num+=romandict[j]
        last=j
    return num
r=input("enter the roman number:\n")
result=romtodec(r)
print(result)