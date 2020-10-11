# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:53:53 2020

@author: stimo
"""
#The Cavern of the Evil Wizard
import time
import random

print('Hello')
time.sleep(1)

def cavern():
    
    weapons = ['thermal pod','crossbow','sword','flail']
    
    def intro():
        gameplay = ""
        while gameplay !="yes":
            gameplay = input("Would you like to play a game? (yes/no): ")
        if gameplay == "yes":
            print("The Adventure Begins!...")
            time.sleep(2)
        else:
            time.sleep(2)
            end
            
            return gameplay


   
    def beginning():
       print("You are standing in the cavern of the evil wizard...")
       time.sleep(2)
       print("All around you are the carcasses of slain ice dwarfs...")
       time.sleep(2)
    
    def wizard():
        print("The wizard stands before you...")
        wizard = input("What would you like to do?: ")
        if wizard == "melt wizard":
            weapon()
        else:
          end()
            
    def weapon():
        weapon = input("what do you want to use against him? ")
        if weapon == "thermal pod":
            print("the thermal pod melts the wizard")
            print("His shrieks of pain shake the cave")
            end()
        elif weapon == "sword":
            print("your sword isnt strong enough against the wizards ice")
            scepter()
        elif weapon == "crossbow":
            print("arrows are no match for my powers!")
            scepter()
        else:
            end()
            
        
            
    def scepter():
        print("The wizards unleashes a fatal bolt from the ice sceptor")
        print("with luck you will thaw in several million years")
        end()


    def end():
        print("Thanks for playing")
        
        
  

cavern()

    
    
        

    
    






