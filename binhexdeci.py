# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:31:20 2023

@author: Chintan c shetty
"""

def bintodec(num):
    dec=0
    i=0
    for dig in num[::-1]:
        dec+=int(dig)*2**i
        i+=1
    return dec
num=input("enter the  binary number to convert into decimal: \n")
result=bintodec(num)
print("binary to decimal:\n",result);
def octtohex(num):
    dec=0
    i=0
    for dig in num[::-1]:
        dec+=int(dig)*8**i
        i+=1
    list=[]
    while dec!=0:
        list.append(dec%16)
        dec=dec//16
    r=[]
    for i in list[::-1]:
        if i<10:
            r.append(str(i))
        else:
            r.append(chr(ord('A')+(i-10)))
    hex="".join(r)
    return hex
num2=input("enter the number to convert into hexadecimal:\n")
result1=octtohex(num2)
print("octadecimal to hexadecimal:\n",result1)
    