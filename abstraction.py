# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:45:17 2024

@author: Chintan c shetty
"""
from abc import ABC,abstractmethod
class vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres=n
    @abstractmethod#it is a decorator for abstract method
    def start(self):
        pass
    def normalmethod(self):
        print("this normal method from abstract class")
class bike(vehicle):
    def __init__(self):
       self.no_of_tyres=2
    def start(self):#here we define abstract method start of vehicle 
        print("start with kick")
class scooty:
    def __init__(self):
        self.no_of_tyres=2
    def start(self):
        print("start with shelf")
class car:
    def __init__(self):
        self.no_of_tyres=4
    def start(self):
        print("start with key")
b=bike()
b.start()
b.normalmethod()