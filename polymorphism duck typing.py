# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:14:51 2024

@author: Chintan c shetty
"""

class duck:
    def swim(self):
        print("I am duck and i can swim ")
    def speaks(self):
        print("quak quak")
class dog:
    def swim(self):
        print("i am dog i can swim")
    def speaks(self):
        print("woof woof")
        
        
def display(dk):#dynamic typing where duck=do and duck=d
    dk.swim()
    dk.speaks()
    print("information displayed")
d=duck()
do=dog()
display(do)#display method is called
display(d)