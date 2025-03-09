# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:47:51 2023

@author: Chintan c shetty
"""
import os.path
import sys
import shutil
f=input("enter the directory path:\n")
a=shutil.make_archive('myzipp','zip',f)
if os.path.isfile('myzipp.zip'):
    print("created zip file sucessfully")
else:
    print("not able archived")
