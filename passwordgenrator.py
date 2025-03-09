# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:41:18 2024

@author: Chintan c shetty
"""
import random
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list =['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '/', '?']
nl=int(input("enter the number letters"))
nn=int(input("enter the number numbers"))
ns=int(input("enter the number symbols"))
password=""
for i in range(nl):
    char=random.choice(alphabet_list)
    password=password+char
for i in range(nn):
    char=random.choice(numbers_list)
    password=password+char
for i in range(ns):
    char=random.choice(symbols_list)
    password=password+char
password_list=list(password)
random.shuffle(password_list)
passwordfinal=''.join(password_list)
print("the genrated password is",passwordfinal)