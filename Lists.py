# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:44:22 2021

@author: munez
"""


def check_zero(N, arr):
    
    # complete the if statement to check
    # if first or last element in list is 0
    if(arr[0]==0 or arr[-1]==0 ):
        return True

    return False

print(check_zero(5,[0,10,23,34,98]))


def print_elements(N, arr):
    for i in range(len(arr)):
        print(arr[i],end=' ')
        
print_elements(5,[23,43,65,78,98])        


def count_even_odd(N, arr):
    c_e = 0
    c_o = 0
    
    pair = list()
    
    for i in arr:
        if i%2==0:
            c_e+=1
        if i%2!=0:
            c_o+=1  
    
    pair.append(c_e)
    pair.append(c_o)
    
    return pair

print(count_even_odd(5, [22,12,34,54,66]))


def calc_average(arr):
    print('Sum is {}'.format(sum(arr)))
    print('Min is {}'.format(min(arr)))
    print('Max is {}'.format(max(arr)))
    print('Average is {}'.format(sum(arr)/len(arr)))
    min_max=min(arr)+max(arr)
    print('Excluding min & max, Average is {}'.format((sum(arr)-min_max)/len(arr)))
    
calc_average([20,3,55])

#Exercise 1: Reverse a given list in Python
def reverse_list(list1):
    print(list(reversed(list1)))

reverse_list([100, 200, 300, 400, 500])

#Exercise 2: Concatenate two lists index-wise
def concat_2list(lst1,lst2):
    lst3=[i+j for i,j in zip(lst1,lst2)]
    print(lst3)
    
concat_2list(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"])

#Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
def return_sqr(list):
    list1=[i**2 for i in list]
    print(list1)
    
return_sqr([1, 2, 3, 4, 5, 6, 7])

#Exercise 4: Concatenate two lists in the following order
def concat(list1,list2):
    list3=[i+j for i in list1 for j in list2]
    print(list3)
    
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concat(list1,list2)

'''
Exercise 5: Given a two Python list. Iterate both lists simultaneously such that
list1 should display item in original order and list2 in reverse order'''

def iterate_2list(list1,list2):
    for i,j in zip(list1,list2[::-1]):
        print(i,j)
        
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate_2list(list1, list2)

#Exercise 6: Remove empty strings from the list of strings

def remove_list(list1):
    res=list(filter(None,list1))
    print(res)

#use of filter to remove None Type 

remove_list(["Mike", "", "Emma", "Kelly", "", "Brad"])

'''Exercise 9: Given a Python list, find value 20 in the list, and if it is present,
replace it with 200. Only update the first occurrence of a value'''

def replacevalue(list1,value):
    index=list1.index(value)
    list1[index]=200
    print(list1)

replacevalue([5, 10, 15, 20, 25, 50, 20], 25)

#Exercise 10: Given a Python list, remove all occurrence of 20 from the list
def revocur(list1):
    for i in list1:
        if i==20:
            list1.remove(i)
    print(list1)

revocur([5, 10, 15, 20, 25, 50, 20])

#generate list of all even no's between 4 & 30 
def even_list(list):
    lst=[]
    for i in range(len(list)):
        if i%2==0:
            lst.append(list[i])
    return lst

print(even_list([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]))
     
#return largest item from the list 
def largest(list):
    return max(list)

print(largest([4, 6, 8, 24, 12, 2]))


#picking an odd-index element from the first list and even index elements from the second
def thirdlist(lst1,lst2):
    lst3=[]
    for i in range(len(lst1)):
        if i%2!=0:
            lst3.append(lst1[i])
    for i in range(len(lst2)):
        if i%2==0:
            lst3.append(lst2[i])
    print(lst3)
thirdlist([3, 6, 9, 12, 15, 18, 21],[4, 8, 12, 16, 20, 24, 28])

#remove the element at index 4 and add it to the 2nd position and at the end of the list
def modify(lst):
    print('Original list',lst)
    item=lst.pop(4)
    print('After Removing 4th index',lst)
    lst.insert(2,item)
    print('After inserting it at 2nd index',lst)
    lst.append(item)
    print('After inserting at last index',lst)   
modify([54, 44, 27, 79, 91, 41])

#divide a list into n Chunks size of list .
def chunk(lst):
    print('original list',lst)
    length=len(lst)
    chunksize=length//3
    start=0
    end=chunksize
    for i in range(1,4,1):
        indexes=slice(start,end,1)
        slicelist=lst[indexes]
        print('Chunk',i,slicelist)
        print('After reversing ',list(reversed(slicelist)))
        start=end
        if i!=2:
            end+=chunksize
        else:
            end+=length-chunksize
            
chunk([11, 45, 8, 23, 14, 12, 78, 45, 89])





    
    


    
    

