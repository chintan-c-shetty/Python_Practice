# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:43:23 2024

@author: Chintan c shetty
"""

class human:
    def __init__(self,num):
        self.eyes=10
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class male():
    def __init__(self,name):
        self.name=name
        self.nostrils=2
    def eat(self):
        print("i love noodles")
    def work(self):
        print("i can code also")
class boy(human,male):
     def __init__(self,name,num):
         self.name=name
         human.__init__(self,num)#we cant use super keys because two parents 
         male.__init__(self,name)
     def eat(self):
         print("i love kebab")
     def work(self):
         print("i can talk")
boy1=boy("jcdhkcdvbhsdg",1)
boy1.eat()
print(boy1.eyes)
print(boy1.nostrils)
print(boy.mro())
