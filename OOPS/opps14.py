# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:27:16 2021

@author: munez
"""

'''
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
Give the complete code for the  BankAccount class.
'''

class BankAccount:
    
    def __init__(self,accnum,name,balance):
        self.accnum=accnum
        self.name=name
        self.balance=balance
        
    def deposit(self,d):
        self.balance=self.balance+d
        return f'Updated balance:{self.balance}'
    
    def withdrawl(self,w):
        if self.balance<w:
            return r'Insufficient Balance'
        else:
             self.balance=self.balance-w
        return f'Withdrawl:{w},Balance:{self.balance}'
    
    def bankfees(self):
        f=self.balance*(5/100)
        return f'The fees is {f}'
    
    def display(self):
        return f'AccountNumber:{self.accnum}\nName:{self.name}\nBalance:{self.balance}'
    
acc1=BankAccount(134267,'Maaz',23000)
acc1.withdrawl(3000)
acc1.deposit(2000)

print(acc1.display())
print(acc1.bankfees())

        