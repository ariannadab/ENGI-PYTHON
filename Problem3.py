# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:52:44 2018

@author: AriannaDabreo
"""

n = int(input("Enter any number: "))

sum1 = 0

for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i

print(sum1==n) #Perfect numbers will print true, otherwise it will return false
               
