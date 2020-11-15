#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:05:34 2020

@author: muhammadzahidi
"""
import time
import random
    
print("-"*70)
print("              ZumTheZazaKing's Paper Scissors Rock Game!")


def main():

    arr = ['paper', 'scissors', 'rock']
    
    compchoice =  random.choice(arr)
    
    print("-"*70)
    print("QTPI (Computer) is choosing...")
    print("-"*70)
    
    time.sleep(2)
    
    print("QTPI has chosen their form of attack!")
    print("-"*70)
    
    time.sleep(1)
    
    plyrchoice = str(input("What will you choose? (Rock, Paper or Scissors?):"))
    print("-"*70)
    
    time.sleep(2)
    
    print("Processing the winner...")
    print("-"*70)
    
    if plyrchoice == 'Paper' and compchoice == 'scissors':
        
        time.sleep(3)
        print("QTPI won this round! Better luck next time!")
        print("-"*70)
        
    elif plyrchoice == 'Paper' and compchoice == 'rock':
        
        time.sleep(3)
        print("You did it! You beat QTPI!")
        print("-"*70)
        
    elif plyrchoice == 'Scissors' and compchoice == 'rock':
        
        time.sleep(3)
        print("QTPI won this round! Better luck next time!")
        print("-"*70)
        
    elif plyrchoice == 'Scissors' and compchoice == 'paper':
        
        time.sleep(3)
        print("You did it! You beat QTPI!")
        print("-"*70)
        
    elif plyrchoice == 'Rock' and compchoice == 'paper':
        
        time.sleep(3)
        print("QTPI won this round! Better luck next time!")
        print("-"*70)
        
    elif plyrchoice == 'Rock' and compchoice == 'scissors':
        
        time.sleep(3)
        print("You did it! You beat QTPI!")
        print("-"*70)
        
    elif plyrchoice == 'Paper' and compchoice == 'paper':
        
        time.sleep(3)
        print("Draw! That was unexpected!")
        print("-"*70)
        
    elif plyrchoice == 'Scissors' and compchoice == 'scissors':
        
        time.sleep(3)
        print("Draw! That was unexpected!")
        print("-"*70)
        
    elif plyrchoice == 'Rock' and compchoice == 'rock':
        
        time.sleep(3)
        print("Draw! That was unexpected!")
        print("-"*70)
        
    else:
        
        time.sleep(2)
        print("""
              This outcome is not supposed to be possible. 
              You must have entered a form of attack incorrectly
              (You probably wrote rock instead of Rock)
              Either way, get out of here
              """)
              
        time.sleep(3)
        
        
        
    
    


while True:
    
    main()
    
    time.sleep(2)
    
    if str(input("Would you like to play again?(Y or N):")).strip().upper() != "Y":
        
        print("\nGoodbye!\n")
        
        time.sleep(1)
        
        break