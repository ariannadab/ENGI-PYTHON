#/usr/bin/python
# -*- coding: utf-8 -*-

import random

class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return (str(self.suit)+' '+str(self.rank)) # replace this line

    def value(self, total):
        if self.rank in range(1,11):
            return self.rank
        elif self.rank in ['J','Q','K']:
            return 10
        else:
            if total<11:
                return 11
            else:
                return 1


def make_deck():

    suits = ['♠','♣','♦','♥']
    num= range(2,11)
    face= ['J','Q','K','A']
    deck = [Card(i,j) for j in num for i in suits]
    deck += [Card(i,j) for j in face for i in suits]
    # use random.shuffle(some_list) to shuffle the deck of cards.
    random.shuffle(deck)

    return deck # replace this line 


def main():
    deck = make_deck()
    psum=0 #player sum
    csum=0 #computer sum
    print("You drew a:"+ str(deck[0]))
    psum+=deck[0].value(psum)
    deck.pop(0)
    print("Your sum is: "+str(psum))
    choice=input("Would you like to draw another card? Y/N ")
    while choice == 'Y':
        print("You drew a:"+ str(deck[0]))
        psum+=deck[0].value(psum)
        deck.pop(0)
        print("Your sum is: "+str(psum))
        if psum<21:
            choice=input("Would you like to draw another card? Y/N ")
        else:
            choice='N'
    
    cchoice='Y'
    print("\nI drew a:"+ str(deck[0]))
    csum+=deck[0].value(csum)
    deck.pop(0)
    print("My sum is: "+str(csum))
   
    while cchoice == 'Y':
        print("\nI drew a:"+ str(deck[0]))
        csum+=deck[0].value(csum)
        deck.pop(0)
        print("My sum is: "+str(csum))
        if csum<17:
            cchoice='Y'
        else:
            cchoice='N'
    
    if psum>21 and csum<=21:
        print("\nSorry, you lose!")
    elif psum<=21 and csum>21:
        print("\nCongrats, you win!")
    elif psum>21 and csum>21:
        print("\nWe both lost!")
    elif (21-psum)<(21-csum):
        print("\nCongrats, you win!")
    elif (21-psum>21-csum):
        print("\nSorry, you lose!")
    elif(psum==csum):
        print("\nIt was a tie!")
    
    
    
        

if __name__ == "__main__":
    main()
