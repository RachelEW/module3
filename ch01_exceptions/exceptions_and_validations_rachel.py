# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:46:42 2019

@author: winkl
"""

#################################
"""Exceptions and Validations"""
#################################

#-------------------------#
"""Task One: Exceptions"""
#-------------------------#

try:
    f = open('testfile.txt') #need the .txt for the file to open, without this it gives an error
except Exception:
    print('Sorry, this file does not exist, of the file name is wrong. Please double check.')

#Use specific exceptions to filter out the error reporting process e.g. change 'Exception' to 'FileNotFoundError'

#-----------------------------------------#
"""Task Two: Using specific Exceptions"""
#-----------------------------------------#

#try:
#    f = open('testfile.txt')
#    s1 = not_exist
#except FileNotFoundError:
#    print('Sorry, this file does not exist, of the file name is wrong. Please double check.')
#except Exception:
#    print('Sorry. Something is wrong after opening function.')
    
#If the specific error "FileNotFound" had not been added the generic "Excpetion" error would have been raised.
#This would have been because of the variable not having been defined but would have not been clear from the error message that the error was not to do with opening the file.
#Specific error messages help to show which part of the function is raising the error.
    
#NB: always put built in/specific exceptions before general excpetions, otherwise the program will only pick up the general exceptions and won't continue to read the code.

#Python has a library of built in exceptions - check this library (link in e-curriculum)
    
#-----------------------------------------------------#
"""Task Three and Four: More testing and using else"""
#-----------------------------------------------------#

try:
    f = open('testfile.txt')
#    s1 = not_exist
except Exception as e:
    print('e')
else:
    print(f.read())
    f.close()
    
#'e' prints for any exception
#else clause is executed if try block does not raise an exception

#-------------------------------------#
"""Task Five: Finally Block"""
#-------------------------------------#


try:
    f = open('testfile.txt')
except Exception as e:
    print('e')
else:
    print(f.read())
    f.close()
finally:
    print('executing finally...')

#finally clause will run regardess of what happens in the try/except block
    
#------------------------------------------#
"""Task Six: Manually raise an Exception"""
#------------------------------------------#

try:
    f = open('testfile.txt')
    if f.anme == 'testfile.txt':
        raise Exception
except Exception as e:
    print('file name is the same')
    

#Example from Mabel

try:
    with open('testfile.txt', 'r') as f:
        f_text = f.read()
    if f.name == 'test.txt':
        # it's better to raise specific errors than generic
        raise OSError('that is the wrong file!')
except Exception as e:
    print(e)
else:
    print(f_text)
finally:
    print('this is the end!')
    

#NB: it is bad practice to have 'catch-all' excpetions - makes it harder to debug as could be hiding another issue in the code
    