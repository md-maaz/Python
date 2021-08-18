# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:23:27 2021

@author: munez
"""

class vehicle:
    
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
        
    def seating_capacity(self,capacity):
        return f'the vehicle name is {self.name} and capacity is {capacity}'
    
veh1=vehicle('Volvo',75,34)
print(veh1.__dict__)
print(veh1.seating_capacity(70))

class bus(vehicle):
    
    def seating_capacity(self,capacity):
        return super().seating_capacity(capacity)
    
bus1=bus('Safari',56,23)
print(bus1.__dict__)
print(bus.__dict__)
print(bus1.seating_capacity(30))
        
