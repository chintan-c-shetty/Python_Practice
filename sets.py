# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 11:50:15 2024

@author: Chintan c shetty
"""

a={1,2,34,5,6,3,4,0}
b={4,5,3,6,7,8,9}
c={1,2,3,4}
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)
print(c.issubset(a))
a.add(45)
print(a)