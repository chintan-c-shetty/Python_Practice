# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:25:22 2023

@author: Chintan c shetty
"""

import re
import os.path
phregx=re.compile(r'\+\d{12}')
emailregx=re.compile(r'[A-Za-z0-9._]+@[A-Za-z]+.[a-z|A-Z]{2,}')
fname=input("enter the file name:")#input example.txt
if os.path.isfile(fname)==False:
            print("file doesnt exists")
else:
 f=open(fname,'r')
 for line in f:
    matche=phregx.findall(line)
    matches=emailregx.findall(line)
print("emails:")
for match in matches:
    print(match)
print("phone numbers:")
for match1 in matche:
    print(match1)
    
    