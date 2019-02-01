# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:50:51 2019

@author: winkl
"""

import unittest
import sys
from unit_testing_rachel import is_prime

"""
#without a class, not efficient (not recommended)
#without a class would have to call each function individually at the end
#with a class you can just create an object at the end to call everything from that class
#"""
#def test_prime(TestCase):
#    TestCase.assertTrue(is_prime(5))
#
"""
##create a class for unit testing, can have many different tests within this
#call the function TestCase, it gives you assertion functionalities (from unittest module)
"""

class prime_test(unittest.TestCase):
    def test_is_prime_float(self):
        self.assertTrue(is_prime(5))
#this hardcodes a certain input e.g. could test what happens for float inputs by hardcoding a float
    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-2))
#after tests fail, the code an be rewritten to make them pass e.g. by adding exceptions

"""
#using sys library means we define the input on the command line when we run the code
#argv[0] is the file we are running (what comes after "python")
#argv[1] is then the first arguement that is named after you type in the file name
"""
        
#    def test_prime(self):
#        self.asserIsInstance(sys.argv[1], int)
#        self.assertTrue(is_prime(sys.argv[1]))
#        
#    def sys_input(self):
#        self.assertInstance(sys.argv[1], int)
#
#if __name__ == "__main__":
#    unittest.main()

"""
#using a function (without a class) to see how it works initially - this doesn't work in Python3, can only use classes
"""

"""
#unittest has a fuction called main which calls all TestCases which you have defined
"""

if __name__ == "__main__":
#It is good pracice to put code you want to run under this main definition. It is the correct syntax.
    unittest.main()

