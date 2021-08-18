# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:03:25 2021

@author: munez
"""

import math

class Point2D:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def  calculate_distance(self,other):
        result=math.sqrt(pow(self.x-other.x,2)+pow(self.y-other.y,2))
        return result
        
point1=Point2D(3,4)
point2=Point2D(9,5)
distance=point1.calculate_distance(point2)
print(distance)

'''----------------------------------------------------------------------'''

class Time:
    
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    
    def total_seconds(self):
        return 3600 * self.hour + 60 * self.minute + self.second
    
    def __str__(self):
        s = ''
        if self.hour < 10:
            s += '0'
        s += str(self.hour)
        s += ':'
        if self.minute < 10:
            s += '0'
        s += str(self.minute)
        s += ':'
        if self.second < 10:
            s += '0'
        s += str(self.second)
        return s
            
time1=Time(9,5,7)
print(time1.total_seconds())
print(time1)

'''------------------------------------------------------------------------'''

class SupermarketQueue:
    
    def __init__(self):
        self.queue=list()
        
    def add_to_back(self,name):
        if name not in self.queue:
            self.queue.append(name)
    
    def remove_from_front(self):
        fp=self.queue.pop(0)
        return fp 
        
    def __str__(self):
        return str(self.queue[::-1])
        
    def __len__(self):
        return len(self.queue)
        
    
queue=SupermarketQueue()
queue.add_to_back('Alice')
queue.add_to_back('Bob')
print(len(queue))
print(queue)
print(queue.remove_from_front())


'''-----------------------------------------------------------------------'''

class User:
    
    def __init__(self,row):
        self.id=row[0]
        self.email=row[1]
        self.name=row[2]
        self.address=row[3]
        
        
users=[]
import csv
with open('user_accounts.csv') as f:
    reader=csv.reader(f)
    rows=list(reader)
    for row in rows[1:]:
        user=User(row)
        users.append(user)
        

last = users[-1]
print(last.id)
print(last.email)
print(last.name)
print(last.address)    

'''------------------------------------------------------------------------'''






        
        
        
        


