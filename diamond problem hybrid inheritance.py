# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:14:17 2024

@author: Chintan c shetty
"""

class a:
    def display(self):
        print("displaying in the a class")
class b(a):
    def display(self):
        print("displaying in the b class")
class c(a):
    def display(self):
        print("displaying in the c class")
class d(b,c):
    def show(self):
        print("displaying in the c class")
d1=d()
d1.display()
print(d.mro())