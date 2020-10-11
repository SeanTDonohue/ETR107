# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:35:07 2020

@author: stimo
"""

from __future__ import print_function, division


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('rotator'))
