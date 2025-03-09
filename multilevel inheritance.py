# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:02:38 2024

@author: Chintan c shetty
"""

class human:
    def  __init__(self ,num):
        print("the calling the human ")
        self.num=num
        print(num)
        self.eyes=2
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can stand")
class male(human):
    def __init__(self,name):
        self.name=name
        print("calling from male")
        #human.__init__(self,name) 
        super().__init__(self.name)
    def sleep(self):
        print("i can sleep whole day")
    def work(self):
            super().work()#human.work() also can be used
            print("i can run")
class boy(male):
     def __init__(self):#if this constructor is not present will search in male
        print("i am grandson")
     def work(self):
         print("i am very lazy")
boy1=boy()# here it searches init function first
boy1.work()
m=male("tharuni")