# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:11:57 2023

@author: Chintan c shetty
"""
n=int(input("enter the number:\n"))
if n==1 or n==0:
    print("neither prime or composite")
else:
    c=0
    for i in(2,n//2):
        if n%i==0:
            c=1
    if c==1:
        print("the number is composite")
    else:
        print("the number is prime")
        