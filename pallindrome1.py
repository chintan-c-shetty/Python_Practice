# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:05:21 2023

@author: Chintan c shetty
"""
def pallindrome(n):
   temp=n
   rev=0
   while temp!=0:
     rev=rev*10+temp%10
     temp=temp//10
   if n==rev:
      print('the entered number is pallindrome')
   else:
     print("not pallindrome")
     
     
def check_num_of_occ(num):
    l=[]
    for i in range(10):
        l.append(0)
    while num!=0:
        dig=num%10
        l[dig]=l[dig]+1
        num=num//10
    for i in range(10):
        if l[i]!=0:
            print(i,"appears",l[i],"times")
num=int(input("enter the number:\n"))
check_num_of_occ(num)
pallindrome(num)
