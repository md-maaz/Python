# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:25:54 2021

@author: munez
"""

'''
Define a Book class with the following attributes: Title, Author (Full name), Price.
Define a constructor used to initialize the attributes of the method with values entered by the user.
Set the View() method to display information for the current book.
Write a program to testing the Book class.
'''

class book:
    
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        
    def view(self):
        print(f'Title:{self.title}\nAuthor:{self.author}\nPrice:{self.price}')
        
book1=book('Water & Ice','Goerge R Martin',250)
book2=book('Mathematics vol1','RD Sharma',600)
book1.view()
book2.view()
