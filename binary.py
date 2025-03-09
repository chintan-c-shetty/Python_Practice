# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:15:15 2023

@author: Chintan c shetty
"""
import sys
list1=[]
n=int(input("enter the size of array:\n"))
print("enter the elements in ascending order:")
for i in range(n):
    list1.append(int(input()))
low=0
high=n-1
key=int(input('enter the key searched:\n'))

while low<=high:
      mid=(low+high)//2
      if key==list1[mid]:
         print("the key is found in  :",mid+1)
         sys.exit(0)
      elif key>list1[mid]:
         low=mid+1
      else:
         high=mid-1

print('entered key is not found')
        