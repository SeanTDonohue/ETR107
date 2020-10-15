# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:26:49 2020

@author: stimo
"""

from microbit import *

steps=0

while True:
    if accelerometer.was_gesture("up"):
        steps += 1
        display.show(steps)
    if button_a.is_pressed():
        steps = 0
        display.show(0)
        
        
        
