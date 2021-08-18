# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 13:44:39 2021

@author: munez
"""

'''
Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor
2 - Define a Area() method of the class which calculates the area of ​​the circle.
3 - Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
4 - Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
'''

class circle:
    
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
        
    def area(self):
        import math 
        area=math.pi * pow(self.r, 2)
        return area
    
    def perimeter(self):
        import math
        per=2*math.pi*self.r
        return per 
    
    def testbelongs(self,c,d,e):
        if c<self.a and d<self.b and e<self.r:
            return r'This belong to circle'
        else:
            return r'Circle does not belong to Original Circle'
        
        
    
c1=circle(3,4,5)
print(c1.r)
print(c1.area())
print(c1.perimeter())
print(c1.testbelongs(1,1,1))