# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:23:58 2021

@author: munez
"""

# CLASS & INSTANCES

class employee:
    
      
    # define init method 
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname + '.' + lname + '@company.com'

#instance
emp1=employee('john','carter',5000)
emp2=employee('damien','darkh',6000)

print(emp1.email)
print(emp2.email)