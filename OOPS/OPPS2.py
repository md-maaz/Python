# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:29:35 2021

@author: munez
"""

# CLASS VARIABLESS

class employee:
    
    #class variable 
    raise_amt=1.1
    num_of_emp=0
    
    # define init method 
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname + '.' + lname + '@company.com'
        
        employee.num_of_emp+=1
    
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

    
print(employee.num_of_emp)

#instance
emp1=employee('md','maaz',9000)
emp2=employee('md','adil',8000)

print(emp1.email)
print(emp2.email)

print(emp1.pay)
print(emp2.pay)

print(emp1.fullname())
print(employee.fullname(emp2))

print(employee.num_of_emp)

#changing value of class variable 
employee.raise_amt=1.5
#print(employee.__dict__)
#assigning instance1 class variable
emp1.raise_amt=2.0
#print(emp1.__dict__)
#assigning instance2 class variable 
emp2.raise_amt=3.0
#print(emp2.__dict__)

#raise without class variable 
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)

#raise with class variable
print(emp1.pay)
emp1.apply_raise1()
print(emp1.pay)

print(emp2.pay)
emp2.apply_raise1()
print(emp2.pay)