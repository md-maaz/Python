# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:22:09 2021

@author: munez
"""

'''
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.
'''

class rectangle:
    
    def __init__(self,length,width):
        self.length=length
        self.width=width

        
    def perimeter(self):
        return f'The Perimeter is {2*(self.length+self.width)}'
    
    def area(self):
        return f'The Area is {self.length*self.width}'
    
    def display(self):
        return f'Length :{self.length}\
                Width :{self.width}\
                Perimeter :{self.perimeter()}\
                Area : {self.area()}'
                
class Parallelepipede(rectangle):
    
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height=height
        
    def volume(self):
        return f'Volume : {self.length*self.width*self.height}'
        
rec1=rectangle(34, 23)        
print(rec1.length)
print(rec1.width)
print(rec1.perimeter())
print(rec1.area())
print(rec1.display())
print(Parallelepipede.__dict__)
para1=Parallelepipede(12, 6, 8)
print(para1.__dict__)
print(para1.volume())


        
        
