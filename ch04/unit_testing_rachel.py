# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:44:03 2019

@author: winkl
"""

def is_prime(number):
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

                 

