# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:05:05 2021

@author: munez
"""

'''
1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
4 - Create a method called testPrims() allowing to test if two numbers are prime between them.
5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.
'''

class Coputation:
    
    def __init__(self):
        pass 
    
    def factorial(self,n):
        factorial=1
        if n<0:
            print('Negative no factorial is Invalid')  
        elif n==0:
            print('Factorial of 0 is 1')    
        else:
            for i in range(1,n+1):
                factorial=factorial*i
            print(f'The factorial of {n} is {factorial}')
            
    def sum(self,n):
        suum=0
        for i in range(1,n+1):
            suum=suum+i
        print(f'The Sum is {suum}')
        
    def testPrim(self,num):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    print(f'{num} is not a prime no')
                    break
            else:
                print(f'{num} is a prime no')
                
    def tableMult(self,num):
        table=[]
        for i in range(1,11,1):
            table.append(num*i)
        print(table)
                    
    def allTablesMult(self,n):
        for x in range(1,n+1):
            table=[]
            for i in range(1,11,1):
                table.append(x*i)
            print(table)
         
    
        
cop1=Coputation()
# print(cop1.__dict__)
# cop1.factorial(5)
# cop1.sum(5)
# cop1.testPrim(4)
# cop1.tableMult(5)
# cop1.allTablesMult(3)

