# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 23:00:04 2024

@author: Chintan c shetty
"""

def multiply_(a,*args,name):
    c=1
    print(name)
    for i in args:
        c=c*i
    print(f"product is{c}")
multiply_(1,1,2,3,4,5,name="chintan")