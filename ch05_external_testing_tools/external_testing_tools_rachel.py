# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:54:22 2019

@author: winkl
"""

#############################
"""External Testing Tools"""
#############################

#----------------------------------------------------------------------#
"""Task One: function to run tests running with pytest and nosetest"""
#----------------------------------------------------------------------#

#class Calculator():
#    
#    def add(self, x, y):
#        number_types = (int, float, complex)
#        if isinstance(x, number_types) and isinstance(y, number_types):
#            return x + y
#        else:
#            raise ValueError
            
#----------------------------------------------------#
"""Task Two: adding mistakes to practise debugging"""
#----------------------------------------------------#
        
class Calculator():
    
    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            import pdb; pdb.set_trace() #new debugging technique
            result = x - y
            print("Results is: {}".format(result))
            return result
        else:
            raise ValueError