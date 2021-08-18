# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:54:10 2021

@author: munez
"""

# SPECIAL(MAGIC/DUNDER) METHODS 

class employee:
    
    # define init method 
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname + '.' + lname + '@company.com'
        
        
    
    #method
    def fullname(self):
        return f'{self.fname} {self.lname}'
    
    def apply_raise(self):
        self.pay=int(self.pay*1.04)
        return self.pay
        
    #lets use the class variable 
    def apply_raise1(self):
        self.pay=int(self.pay * self.raise_amt)
        return self.pay
    
    def __repr__(self):
        return "employee('{}','{}','{}')".format(self.fname,self.lname,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self,other):
        return self.pay+other.pay

#instance
emp1=employee('john','carter',5000)
emp2=employee('damien','darkh',6000)

print(emp1)

print(emp1+emp2)
    