# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:07:53 2021

@author: munez
"""

#create a vehicle class 
class vehicle:
    
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage

#create a class without any variables & methods
class vehicle1:
    pass
        
#create a class BUS , that will inherit all variables & methods of vehicle class
class bus(vehicle):
    pass



veh1=vehicle('volvo',75,34)
print(veh1.__dict__)
print(veh1.speed)
print(veh1.mileage)

bus1=bus('safari',45,12)
print(bus1.__dict__)
print(bus1.name)
