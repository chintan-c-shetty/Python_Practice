# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:23:07 2023

@author: Chintan c shetty
"""
import math
class shape:
    def __init__(self):
        self.name=""
        self.area=0
    def showarea(self):
        print("the area of ",self.name," is ",self.area," units")
class Cricle(shape):
    def __init__(self,radius):
        self.name="Cricle"
        self.radius=radius
    def calarea(self):
        self.area=self.radius*self.radius*math.pi
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.name="rectangle"
    def calarea(self):
        self.area=self.breadth*self.length
class Triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        self.name="Triangle"
    def calarea(self):
        self.area=0.5*self.height*self.base
r=int(input("enter the radius of circle:\n"))
l=int(input("enter the length rectangle:\n"))
b=int(input("enter the breadth rectangle:\n"))
h=int(input("enter the heigth triangle:\n"))
ba=int(input("enter the base triangle:\n"))
c=Cricle(r)
rc=Rectangle(l,b)
t=Triangle(h,ba)
c.calarea()
rc.calarea()
t.calarea()
c.showarea()
rc.showarea()
t.showarea()


    