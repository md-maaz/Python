# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 09:35:28 2021

@author: munez
"""

# CLASS INHERITANCE

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

#class inheritance 
class developer(employee):
    #changing class variable in sub class 
    raise_amt=1.8
    
    def __init__(self,fname,lname,pay,prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang=prog_lang
        
#second class inferitance
class manager(employee):
    
    def __init__(self,fname,lname,pay,employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees 
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())
        
    

#instance
emp1=employee('md','maaz',9000)
emp2=employee('md','adil',8000)
#inhertited class instances
dev1=developer('md','maaz',9000,'Sql')
dev2=developer('md','adil',8000,'python')

mgr_1=manager('Bala','Rao',20000)

print(isinstance(mgr_1, manager))
print(isinstance(dev1,manager))
print(issubclass(developer,employee))
print(issubclass(manager,employee))
print(issubclass(employee,developer))

print(mgr_1.fullname())
print(mgr_1.pay)
print(mgr_1.apply_raise1())
mgr_1.add_emp(emp2)
mgr_1.remove_emp(emp2)
mgr_1.add_emp(dev2)
mgr_1.print_emp()
