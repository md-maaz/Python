# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:52:09 2021

@author: munez
"""

def print_fun():
    print('Hello World')
    
print_fun()

def comma():
    print('Geeks','For','Geeks')
    
comma()

def seperator():
    print('Geeks','For','Geeks',sep='$',end='\n')
    
seperator()

x=5
string='Geeks'
def repetitive(string,x):
    print(string*x,end='\n')
    
repetitive(string, x)

def string_concat(string1,string2):
    print(string1+string2)
    
string1='Welcome '
string2='Jurgen Klopp'
    
string_concat(string1, string2)

def type_cast():
    a=int(input('Enter a integer'))
    b=str(input('Enter a string'))
    c=float(input('Enter a float value'))
    d=bool(input('Enter a boolean value'))
    
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    
type_cast()

def take_input():
    a=input('Enter string 1')
    b=input('Enter string 2')
    c=input('Enter String 3')
    
    print(a,b,c)
    
take_input()


def nsplit():
    string=input('Enter the string ')
    s,i,f=string.split(' ')[0],int(string.split(' ')[1]),float(string.split(' ')[2])
    
    print(type(s))
    print(type(i))
    print(type(f))
    
nsplit()



def print_func():
    print ("Geeks For Geeks")
    
    print ("Geeks Quiz")
    print ("Geeks")
    print ("Geeks For")
    
    
print_func()




def operation(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    e=x//y
    f=x**y
    
    print(a,b,c,d,e,f)
    
operation(20, 10)



def comparision(x,y):
    
    a=(x==y)
    b=(x>y)
    c=(x!=y)
    d=(x<y)
        
    print(a,b,c,d)
    
comparision(20, 20)

def logical(x,y):
    
    a=x and y 
    b=x or y
    c=not a 
    
    print(a,b,c)
    
logical(6, 5)

def do_oeration(x,y):
    
    x-=1
    y+=1
    
    print(x,y,sep='\n')
    
do_oeration(8, 90)

def bitwise(x,y,z):
    
    a = x ^ x
    b = z ^ y
    c = x & y
    d = z | (x ^ x)
    e = ~ b
    
    print(a,b,c,d,e,sep='\n')
    
bitwise(8, 4, 2)


#take input & print it 
def take_input():
    name=str(input('Enter the name:'))
    age=int(input('Enter the age'))
    print('Name',name,'Age',age)
    
take_input()

#print the arguments in a function
def arguments(*args):
    for i in args:
        print(i,end='\n')
        
arguments(20,40,60)

#perform addition & subtraction , return in a single call 
def calculation(a,b):
        
    addition=a+b
    subtraction=a-b 
    
    print(addition,subtraction,sep=',')

a=10
b=20
calculation(a, b)

#default value set 
def showemployee(name,salary=9000):
    print('Name :',name,'Salary :',salary)
    
showemployee('Maaz',9000)
showemployee('Ali')

#create 2 nested functions 
def outer(a,b):
    
    def inner():
        addition=a+b
        return addition
        
    result=inner()+5
    return result

print(outer(10,15))

# function to calculate sum of 0 to n 
def cursive(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+i
    print(sum)
        
cursive(10)

#recursive func to add from 0 to n . 
def recursive(num):
    if num:
        return num+recursive(num-1)
    else:
        return 0 
    
res=recursive(10)
print(res)        

#calling function with a different name ,assignment of a function
def displaystudent(name,age):
    print(name,age)
    
displaystudent('Maaz', 24)

showstudent=displaystudent

showstudent('Emma', 26) 