# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:08:43 2018

@author: AriannaDabreo
"""
time_entered=int(input("Please enter an amount of seconds in between 1 and 86,400 (Inclusive):\t"))

print("Time Entered: ",time_entered," seconds")

if time_entered<0 or time_entered>86400:
    while time_entered<0 or time_entered>86400:
        time_entered=int(input("Please enter a valid amount of seconds."))
else:
    hours=int(time_entered/3600)
    minutes=int((time_entered%3600)/60)
    seconds=int(((time_entered%3600)%60))
    
print("Hours: ",hours," Minutes: ",minutes," Seconds: ",seconds)


    
