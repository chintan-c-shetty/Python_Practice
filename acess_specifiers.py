# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:08:12 2024

@author: Chintan c shetty
"""

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self._age=age#protected _varname
        self.__marks=marks#private __varname
    def display(self):
        print(f"hi my name is {self.name} from student class with marks {self.__marks}")
class branch(student):
    pass
b1=branch("rita",34,91)
b1.display()
print(b1._age)
print(dir(b1))#name mangling


#we dont have special keywords to specify the access modifiers