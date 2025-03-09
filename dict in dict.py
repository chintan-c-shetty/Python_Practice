# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:24:13 2024

@author: Chintan c shetty
"""
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]

for dict in people:
    for key in dict:
        print(f"{key}:{dict[key]}")
        
for dict in people:
    print(dict['name'])