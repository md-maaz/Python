# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:22:56 2021

@author: munez
"""

#random Data generation

import random 

#Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

def start(num):
    for i in range(num):
        print(random.randrange(100,999,5))
        
start(4)

'''
Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets 
and pick two lucky tickets from it as a winner.
'''

def lottery(num):
    lotterylist=[]
    for i in range(num):
        lotterylist.append(random.randrange(1000000000,9999999999))
        
    lucky_draw=random.sample(lotterylist, 2)
    
    print('The lucky dray winners are :',lucky_draw)

#use of sample 
lottery(100)

#Exercise 3: Generate 6 digit random secure OTP

import secrets 

def get_otp():
    secretgenerator=secrets.SystemRandom()
    print('Generating 6 digit OTP')
    otp=secretgenerator.randrange(100000,999999)
    print('The secure OTP is',otp)
     
    
# use of secrets , SystemRandom()
get_otp()

#Exercise 4: Pick a random character from a given String

def random_string(string):
    print('The String is :',string)
    
    print('The random character :',random.choice(string))
    
# use random.choice , choses a random element from a non-empty sequence 
random_string('PYnative')

#Exercise 5: Generate  random String of length 5

def random_string1(stringlength):
    print('Get the letters from String Module')
    letters=string.ascii_letters
    for i in range(stringlength):
        return ''.join(random.choice(letters) for i in range(stringlength))

#use of ascii_letters 
print('The random string is :',random_string1(10))


#Exercise 6: Generate a random Password which meets the following conditions
import string

def randompassword():
    source=string.ascii_letters+string.digits+string.punctuation
    password=random.sample(source,6)
    password+=random.sample(string.ascii_uppercase,2)
    password+=random.sample(string.digits,1)
    password+=random.sample(string.punctuation,1)
    
    
    passwordlist=list(password)
    random.SystemRandom().shuffle(passwordlist)
    password=''.join(passwordlist)
    return password 

print('The password is : ',randompassword())

#Exercise 7: Calculate multiplication of two random float numbers

def mul_two():
    num1=random.random()
    print('Number 1 is ',num1)
    num2=random.uniform(9.5, 99.5)
    print('Number 2 is ',num2)
    
    num3=num1*num2
    print('The multiplication product is :',num3)

# use uniform and random 
mul_two()

#Exercise 9: Roll dice in such a way that every time you get the same number

def rolldice(dice):
    
    for i in range(5):
        random.seed(25)
        print(random.choice(dice))
        
rolldice([1,2,3,4,5,6])

#------------------------------------------------------------------------------

import numpy as np 

#Exercise 1: Create a 4X2 integer array and Prints its attributes

def ex1():
    firstarray=np.empty([4,2,],dtype=np.uint16)
    
    print(firstarray)
    print('Shape is ',firstarray.shape)
    print('Dimension',firstarray.ndim)
    print('ItemSize',firstarray.itemsize)
    

ex1()

'''
Exercise 2: Create a 5X2 integer array from a range between 100 to 200
such that the difference between each element is 10
'''

def ex2():
    secondarray=np.arange(100,200,10)
    secondarray.reshape(5,2)
    print('Second Array is ',secondarray)
    
ex2()

'''
Exercise 3: Following is the provided numPy array.
Return array of items by taking the third column from all rows
'''

def ex3(array):
    print(array[:,-1])
    
sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

ex3(sampleArray)

'''
Exercise 4: Return array of odd rows and even columns from below numpy array
'''

def ex4(array1):
    print(array1[0::2,1::2])
    
sampleArray1 = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

ex4(sampleArray1)

'''
Exercise 5: Create a result array by adding the following two NumPy arrays.
Next, modify the result array by calculating the square of each element
'''

def ex5(arr1,arr2):
    arr3=np.add(arr1,arr2)
    arr3=arr3**2
    print(arr3)
    
arr1 = np.array([[5, 6, 9], [21 ,18, 27]])
arr2 = np.array([[15 ,33, 24], [4 ,7, 1]])

ex5(arr1,arr2)

#Exercise 6: Split the array into four equal-sized sub-arrays

def ex6():
    arr=np.arange(10,34,1).reshape(8,3)
    subarr=np.split(arr,4)
    print('Original Array is ',arr)
    print('After splitting \n',subarr)
    
ex6()

'''
Exercise 7: Sort following NumPy array
Case 1: Sort array by the second row
Case 2: Sort the array by the second column
'''

def ex7(arr):
    print('The Array is ',arr)
    rowarr=arr[:,arr[1:].argsort()]
    print('The array sorted by 2nd row ',rowarr)
    colarr=arr[arr[:,1].argsort()]
    print('The array sorted by 2nd columns ',colarr)
    
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

ex7(sampleArray)

'''
Exercise 8: Print max from axis 0 and min from axis 1 from the following 2-D array.
'''

def minmax(arr):
    print('The array is ',arr)
    arrmin=arr.min(axis=1)
    print('The min of the array is ',arrmin)
    arrmax=arr.max(axis=0)
    print('The max of array is ',arrmax)
    
sampleArray3 = np.array([[34,43,73],[82,22,12],[53,94,66]])

minmax(sampleArray3)

'''
Exercise 9: Delete the second column from a given array 
and insert the following new column in its place.
'''

def ex9(arr):
    print('The array is \n',arr)
    arr=np.delete(arr,1,axis=1)
    print('The array after deleting \n',arr)
    arr=np.insert(arr,1,subarr,axis=1)
    print('The array after inserting is \n',arr)
    
subarr=np.array([10,10,10])
sampleArray4=np.array([[34,43,73],[82,22,12],[53,94,66]])

ex9(sampleArray4)

import matplotlib.pyplot as plt 


#Exercise 10: Create two 2-D arrays and Plot them using matplotlib

def ex10():
    arr=np.random.random_sample(6).reshape(2,3)
    plt.plot(arr)
    plt.show()
    
ex10() 