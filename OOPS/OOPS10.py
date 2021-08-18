# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:12:20 2021

@author: munez
"""

class vehicle:
    
    def __init__(self,name,mileage,capacity):
        self.name=name
        self.mileage=mileage
        self.capacity=capacity
        
    def fare(self):
        return f'The vehicle fare is {self.capacity*100}'
    
class bus(vehicle):
    
    def fare(self):
        total_fare=super().fare()+(super().fare()*0.1)
        return f'Total bus fare is {total_fare}'
    
    
print(bus.__dict__)
bus1=bus('Volovo', 12, 50)
print(bus1.__dict__)
print(bus1.name)
print(bus1.fare())

veh1=vehicle('Rajdhani', 20, 45)
print(veh1.__dict__)
print(veh1.fare())
