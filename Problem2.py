# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:39:52 2018

@author: AriannaDabreo
"""

current_population=307357870

year=int(input("How many years from today would you like to estimate the population for?\t"))

if year<0:
    while year<0:
        year=int(input("Please enter a valid amount.\t"))
        
number_of_seconds=year*365*24*60*60 #total amount of seconds in the year

total_births=int(number_of_seconds/7) #new birth every 7 seconds
print("\nTotal Number of Births: ",total_births)

total_deaths=int(number_of_seconds/13) #death every 13 seconds
print("Total Number fo Deaths: ",total_deaths)

total_immigrants=int(number_of_seconds/35) #immigrant every 35 seconds
print("Total Number of Immigrants: ",total_immigrants)

total_population=current_population+total_births+total_immigrants-total_deaths

print("\nTotal Population After",year,"years: ",total_population)
        
        