# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:16:41 2021

@author: munez
"""

#Exercise 1: Below are the two lists convert it into the dictionary

def convert(list1,list2):
    dic=dict()
    for key,value in zip(list1,list2):
        dic[key]=value
    print(dic)
    
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

convert(keys,values)

#Exercise 2: Merge following two Python dictionaries into one

def merge(dict1,dict2):
    dict3=dict()
    for i,j in zip(dict1,dict2):
        dict3[i]=dict1.get(i)
        dict3[j]=dict2.get(j)
    print(dict3)
    
# can also use dict3={**dict1,**dict2}
    
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
merge(dict1,dict2)

#Exercise 3: Access the value of key ‘history’ from the below


sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}


print(sampleDict['class']['student']['marks']['history'])

#Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

def set_default(keys,default):
    dict2=dict.fromkeys(keys,default)
    print('Dictionary from keys , with default values',dict2)
    
#use fromkeys to intialize a dict with keys & default value    
set_default(employees,defaults)

'''Exercise 5: Create a new dictionary by extracting the
following keys from a below dictionary'''

def extracting(dict1,key):
    for item1 in dict1:
        if item1 in key:
            new_dict={}
            new_dict[item1]=dict1[item1]
        print(new_dict)
            
            
    
    
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"}
key=["name", "salary"]
    
extracting(sampleDict, key)

#Exercise 6: Delete set of keys from a dictionary

def del_key(dict2,key):
    for item2 in key:
        if item2 in dict2.keys():
            dict2.pop(item2)
            
    print(dict2)
    
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"}
key=["name", "salary"]

del_key(sampleDict,key)

#Exercise 7: Check if a value 200 exists in a dictionary

def check(dict3,value):
    flag=False 
    for val in dict3.values():
        if val==value:
            flag=True
    return flag
    
sampleDict1 = {'a': 100, 'b': 200, 'c': 300}
value=100
print(check(sampleDict1, value))

#Exercise 8: Rename key city to location in the following dictionary

def city2loc(dict4,key,newkey):
    print('Dictionary before Pop',dict4)
    dict4[newkey]=dict4.pop(key)
    print('Dictionary After modify',dict4)

sampleDict2 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
key='city'
newkey='location'

#use pop to store the key value to New key 
city2loc(sampleDict2, key, newkey)

#Exercise 9: Get the key of a minimum value from the following dictionary

def get_min(dict5):
    print('The Dictionary is',dict5)
    min_value=min(dict5.values())
    for item in dict5:
        if dict5[item]==min_value:
            print('Key with lowest value:',item)

sampleDict3 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

get_min(sampleDict3)



# SETS ARE UNORDERED

#Exercise 1: Add a list of elements to a given set

def add2set(set1,list1):
    print('Set is :',set1)
    for item in list1:
        set1.add(item)
    print('After addition :',set1)
sampleSet = {"Yellow", "Orange", "Black"}
sampleList2 = ["Blue", "Green", "Red"]
add2set(sampleSet, sampleList2)

#Exercise 2: Return a new set of identical items from a given two set

def identical(set1,set2):
    set3=set1.intersection(set2)
    print(set3)
    
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
identical(set1,set2)

#Exercise 3: Returns a new set with all items from both sets by removing duplicates

def all(set1,set2):
    set3=set1.union(set2)
    print(set3)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
all(set1,set2)

'''
Exercise 4: Given two Python sets,
update the first set with items that exist only in the first set 
and not in the second set.
'''
def check1(set1,set2):
    #check for common value bw sets 
    set1.difference_update(set2)
    print(set1)
        
set1 = {10, 20, 30}
set2 = {20, 40, 50}
check1(set1,set2)

#Exercise 5: Remove items 10, 20, 30 from the following set at once

def removeonce(set1):
    set1.difference_update({10,20,30})
    print(set1)

set1 = {10, 20, 30, 40, 50}

removeonce(set1)

#Exercise 6: Return a set of all elements in either A or B, but not both

def not_accepted(set1,set2):
    set3=set1.symmetric_difference(set2)
    print(set3)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}  

not_accepted(set1, set2)      

'''
Exercise 7: Check if two sets have any elements in common.
If yes, display the common elements.
'''

def displaycommon(set1,set2):
    print(set1.intersection(set2))
    
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

displaycommon(set1, set2)

#Exercise 8: Update set1 by adding items from set2, except common items

def update(set1,set2):
    print(set1.symmetric_difference(set2))
    
set11 = {10, 20, 30, 40, 50}
set22 = {30, 40, 50, 60, 70}

update(set11,set22)

#Exercise 9: Remove items from set1 that are not common to both set1 and set2

def notcommon(set1,set2):
    set1.intersection_update(set2)
    print(set1)
    
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

notcommon(set1,set2)




#Iterate a given list and count the occurrence of each element
def store_dict(lst):
    res=dict()
    for i in lst:
        cnt=lst.count(i)
        res[i]=cnt
    print(res)
    
store_dict([11, 45, 8, 11, 23, 45, 23, 45, 89])


#Given a two list of equal size create a Python set such that it shows the element from both lists in the pair
def introduce_set(lst1,lst2):
    res=zip(lst1,lst2)
    result=set(res)
    print(result)

First_List =[2, 3, 4, 5, 6, 7, 8]
Second_List =[4, 9, 16, 25, 36, 49, 64]
introduce_set(First_List,Second_List)

#Given the following two sets find the intersection and remove those elements from the first set
def intesect(set1,set2):
    set3=set1.intersection(set2)
    print('Intersection Set',set3)
    for i in set3:
        set1.remove(i)
    print('After Intersection Set 1:',set1)

First_Set= {65, 42, 78, 83, 23, 57, 29}
Second_Set ={67, 73, 43, 48, 83, 57, 29}
intesect(First_Set,Second_Set)
        
#Given two sets, Checks if One Set is a subset or superset of another Set. if the subset is found delete all elements from that set
def sub_super_set(set1,set2):
    print('Set1 is sbuset of set2',set1.issubset(set2))
    print('Set2 is subset of set1',set2.issubset(set1))
    
    print('Set is is superSet of set2',set1.issuperset(set2))
    print('Set2 is superset of set2',set2.issuperset(set1))
    
    if set1.issubset(set2):
        set1.clear()
    if set2.issubset(set1):
        set2.clear()
        
    print('Set1',set1)
    print('Set2',set2)
    
firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
sub_super_set(firstSet,secondSet)
    
#Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list
def check_value(list,dict):
    for item in list:
        if item in dict.values():
            list.remove(item)
    print(list)

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
check_value(rollNumber,sampleDict)

# Given a dictionary get all values from the dictionary and add them to a list but don’t add duplicates
def add_list(dict):
    values=set()
    for item in dict.values():
        values.add(item)
    result=list(values)
    print(result)
speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
add_list(speed)

# Remove duplicate from a list and create a tuple and find the minimum and maximum number
def min_max(list):
    items=set()
    for item in list:
        items.add(item)
    result=tuple(items)
    print('Tuple',result)
    print('Max',max(result))
    print('Min',min(result))
    
sampleList1 = [87, 45, 41, 65, 94, 41, 99, 94]
min_max(sampleList1)
