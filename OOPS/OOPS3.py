# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:37:02 2021

@author: munez
"""

# CLASS_METHODS & STATIC_METHODS

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
    
    #class method
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amt=amount
        
    #class method as alternative constructor
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    
    #static method
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False 
        return True 
    
    
#instance
emp1=employee('md','maaz',9000)
emp2=employee('md','adil',8000)
#assigning class variable a new value via class method 
employee.set_raise_amount(1.8)
print(employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
#creating a class constructor 
emp_str_1='md-saif-7000'
new_emp_1=employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
print(employee.num_of_emp)
#create a date variable 
import datetime
week_day=datetime.date(2019, 11, 25)
#checking static method 
print(employee.is_workday(week_day))