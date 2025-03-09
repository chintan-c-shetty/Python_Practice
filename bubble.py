# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:16:11 2023

@author: Chintan c shetty
"""
n=int(input("enter the size of array:\n"))
l=[]
for i in range(n):
    l.append(int(input()))
for i1 in range(n):
    for j in range(0,n-1):
        if l[j+1]<l[j]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)