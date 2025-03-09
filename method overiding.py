# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:50:44 2024

@author: Chintan c shetty
"""

class father:
    def sleep(self):
        print("sleeps from 10:00 pm to 5:00am")
    def eat(self):
        print("eating")
        
class son(father):
    def sleep(self):
        print("sleeps from 12:00 am to 7:00am")
        super().sleep()
s=son()
print(s.sleep())