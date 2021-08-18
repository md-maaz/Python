# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:29:27 2021

@author: munez
"""

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(issubclass(Bus,Vehicle))
print(issubclass(School_bus,Bus))

print(isinstance(School_bus, Bus))
print(isinstance(School_bus, Vehicle))