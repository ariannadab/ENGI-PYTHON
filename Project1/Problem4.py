# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:08:13 2018

@author: AriannaDabreo
"""
import random

guess_number=0

random_value=random.randint(1,10)
    
user_guess=int(input("Guess a number between 1 and 10:\t"))

for guess_number in range (1,5):
    if abs(user_guess-random_value==0):
        print("Congrats, you win!")
        print("The number was: ",random_value)
        break
    elif abs(user_guess-random_value)>5:
        guess_number+=1
        print("Not even close.")
        print("Number of Guesses Left: ",6-guess_number)    
    elif abs(user_guess-random_value)>=3 and abs(user_guess-random_value)<=5:
        guess_number+=1
        print("Close")
        print("Number of Guesses Left: ",6-guess_number)
    else:
        guess_number+=1
        print("Almost there.")
        print("Number of Guesses Left: ",6-guess_number)
    user_guess=int(input("Guess a number between 1 and 10:\t"))

if guess_number==5:
    if abs(user_guess-random_value==0):
        print("Congrats, you win!")
        print("The number was: ",random_value)
    elif abs(user_guess-random_value)>5:
        guess_number+=1
        print("Not even close.")
        print("Number of Guesses Left: ",6-guess_number)    
    elif abs(user_guess-random_value)>=3 and abs(user_guess-random_value)<=5:
        guess_number+=1
        print("Close")
        print("Number of Guesses Left: ",6-guess_number)
    else:
        guess_number+=1
        print("Almost there.")
        print("Number of Guesses Left: ",6-guess_number)        
        

if guess_number>5:
    print("\nYou lose!")
    print("The number was: ",random_value)
    
        
        
        
#random.choice([1,2,3,4,5,6,7,8,9,10])
#random.randint(1,10)
#while x in range(1,6)
            
                
            
            
