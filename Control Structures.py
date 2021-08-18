# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:57:01 2021

@author: munez
"""

def number_present(num_list, Q):
    for i in range(len(num_list)):
        if num_list[i]  in  Q:
            return True
    return False 

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Q = [3, 6, 8, 12]
number_present(num_list, Q)

def friends_in_trouble(j_angry, s_angry):
    
    if j_angry==True & s_angry==True:
        print('You are in Trouble')
    elif j_angry==False & s_angry== False :
        print('You are in trouble')
    else:
        print('You are Not in Trouble')
        
friends_in_trouble(False, False)

def checkOddEven(x):
    
    if x%2==0:
        print(' No is Even ')
    else:
        print(' no is odd ')
    
checkOddEven(3)

def check_status(a, b, flag):
    
    #flag=False
    
    if ((a>=0 & b<0) & flag==False):
        print('a is positive, Status is true')
    elif ((a<0 & b>=0) & flag==False):
        print('b is positive, Status is True')
    elif (a<0 & b<0 & flag==True):
        print('both no are negative , Status is True')
    else:
        print('Status is Fasle')
 
a,b=-2,3
flag=False  
 
check_status(a, b, flag)

def multiplicationTable(n):
    
    for i in range(1,11):
        product=n*i
        print(product,end='\t')
        
multiplicationTable(5)

def stringJumper(st):
    for i in range(0,len(st),2):
        print(st[i], sep=',', end=' ')
        
st='MaytheForcebewithyou'        
stringJumper(st) 

  
def printInDecreasing(x):
    while(x>=0):
        print(x,end='\n')
        x-=1   
printInDecreasing(3) 


def jumpwithwhile(x):
    i=1
    while (i**2<=x):
        print(i**2,end='\t')
        i+=1

jumpwithwhile(100)  

#zero converter

def pos(n):
    
    while(n!=0):
        print(n,sep='\t')
        n-=1
    print(n,sep='\t')
pos(3)

def neg(n):
    while(n!=0):
        print(n,end='\n')
        n+=1
    print(n)

neg(-4)

def cat_hat(st):
    cat = 0
    hat = 0
    for i in range(0, len(st)-2, 1):
        if(st[i : i + 3] == "cat"):
            cat += 1
        if(st[i : i + 3] == "hat"):
            hat += 1
    if(cat == hat):
        print(cat==hat)
    else:
        print(False)

st='catandhat'
cat_hat(st)

def isprime(n):
    
    if n<=1:
        print('No is equal to 1 or less than 1')
        
    for i in range(2,n):
        if n%i == 0:
            print('not a prime no')
            
isprime(5)            
