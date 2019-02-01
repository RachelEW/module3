# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:02:49 2019

@author: winkl
"""

import unittest
from external_testing_tools_rachel import *

class TestCalculatorExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)
    
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
    
    def test_calculator_return_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        
if __name__ == "__main__":
    unittest.main()