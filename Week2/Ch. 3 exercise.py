# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:12:24 2020

@author: stimo
"""
#3.1 exercise
def right_justify():
    print("                                                                 s")
    
right_justify()

#3.2 exercise

def do_twice(f, g):
    f()
    g()


    def print_spam():
        print("spam")
    
    def print_inbox():
        print("Go")
    

    def print_twice(bruce):
        print(bruce)
        print(bruce)

do_twice(print_twice, print_twice)


