# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:59:55 2021

@author: munez
"""

'''
Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student  which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
Create a student object via an instantiation on the Student class and then test the displayStudent method.
'''

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        return f'Name :{self.name}\nAge :{self.age}'

class student(Person):
    
    def __init__(self, name, age,section):
        super().__init__(name, age)
        self.section=section
    
    def displaystudent(self):
        return f'Name:{self.name},Age:{self.age},Section:{self.section}'
        
per1=Person('Maaz',25)
std1=student('Rahul',23,'CSE1')
print(per1.display())
print(std1.displaystudent()) 
    