# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:41:44 2024

@author: Chintan c shetty
"""

class demo:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):#in pyhton method overloading is not alowed 
        return a+b+c
d=demo()
print(d.add(2,3))
print(d.add(2,3,4))#the latest one considered