# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:58:07 2023

@author: Chintan c shetty
"""
import sys
n=int(input("enter the number to the perfect:\n"))
limit=n//2+2
for i in range(limit):
    if i*i==n:
        print("the perfect square of ",i)
        sys.exit(0)
print("not a perfect square")