# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:47:42 2021

@author: munez
"""

class Vehicle:
    
    #class variable
    default_color='White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    
    def __init__(self, name, max_speed, mileage,color='White'):
        super().__init__(name, max_speed, mileage)
        self.color=color
        
    def bus_detail(self):
        return f'Color :{self.color},name:{self.name} speed:{self.max_speed} mileage:{self.mileage}'

class Car(Vehicle):
    
    def __init__(self, name, max_speed, mileage,color='White'):
        super().__init__(name, max_speed, mileage)
        self.color=color
     
    def car_detail(self):
        return f'Color :{self.color},name:{self.name} speed:{self.max_speed} mileage:{self.mileage}'
        
    

bus1=Bus('Volvo',45,23)
print(bus1.bus_detail())
car1=Car('Lamborgini',230,45,'Red')
print(car1.__dict__)
print(car1.car_detail())
