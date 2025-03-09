# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:50:23 2024

@author: Chintan c shetty
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:08:12 2024

@author: Chintan c shetty
"""

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self._age=age#protected _varname
        self.__marks=marks#private __varname
    def get_marks(self):#getter
        return self.__marks
    def set_marks(self,marks):#setter
        self.__marks=marks
   
        #herr we are using a public method for acessing private data
#
b1=student("rita",34,91)

b1.set_marks(98)#setter
print(b1.get_marks())#getter

#we dont have special keywords to specify the access modifiers