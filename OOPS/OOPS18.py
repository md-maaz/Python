# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:43:02 2021

@author: munez
"""

'''
Write a Geometry class with default constructor having no parameters.
Write a methode in Geometry class called distance() that allow to compute a distance between two points A = (a1, a2), B = (b1, b2) (with the convention: a point M is identified with its pair of coordinates M = ( x, y)).
Write a methode in Geometry class called middle() allowing to determine the midle of bipoint (A,B).
Write method called trianglePerimeter() allowing to compute the perimeter of triangle
Write method called triangleIsoscel() which returns a True if the triangle is isoscel and False if not.
'''

class Geometry:
    
    def __init__(self):
        pass
    
    def distance(self,x1,y1,x2,y2):
        import math
        result=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
        print(f'The distance between 2 points is {result}')
        
    def middle(self,a,b):
        middle_point=(a+b)/2
        print(middle_point)
        
    def trianglePerimeter(self,length,width,height):
        print(f'Perimeter is {length+width+height}')
        
    def triangleIsoscel(self,length,width,height):
        if length==width or width==height:
            return True
        return False 
        
geo1=Geometry()
geo1.distance(3,4,7,8)
geo1.middle(2,7)
geo1.trianglePerimeter(3,4,5)
print(geo1.triangleIsoscel(2,2,4))


    