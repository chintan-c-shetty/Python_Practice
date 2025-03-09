# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:47:04 2024

@author: Chintan c shetty
"""

class human:
    def __init__(self):
        self.eyes=10
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class male(human):
    def __init__(self,name):
        super().__init__()# used acess constructor of the parent class
        self.name=name
    #def eat(self):
       # super().eat()
        #print("i love noodles")
    def work(self):
        super().work()
        print("i can code also")
m1=male("jenney")
print(m1.eyes)
m1.eat()
m1.work()