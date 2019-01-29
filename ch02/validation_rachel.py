## -*- coding: utf-8 -*-
#"""
#Created on Wed Jan 23 09:22:42 2019
#
#@author: winkl
#"""
#
#####################
#"""Validation"""
#####################
#
##----------------------------#
#"""Task One: User Input"""
##----------------------------#
#
#print('What is your age?')
#Age = input()
#
##with a space
#
#Age = input('What is your age?')
#
##------------------------------------#
#"""Task Two: Cast to int data type"""
##------------------------------------#
#
#print('What is your age?')
#age = int(input())
#type(age)
#
##-------------------------------------------------#
#"""Task Three: changing input to fit validation"""
##-------------------------------------------------#
#
#Option = input('Please input yes or no ').lower()
#
##----------------------------------------#
#"""Task Four: Validating String Length"""
##----------------------------------------#
#
#while True:
#    five_letter_word = input('Please give a five letter word ')
#    while len(five_letter_word) != 5:
#        five_letter_word = input('Your input was not five letters. Please give a five letter word ')
#    break
#print('Your word is: ',five_letter_word)
#
##While True creates an infinite loop until the conditions are satisfied
#
##OR
#
#userInput = input('Please give a three letter word ')
#if len(userInput)  != 3:
#    userInput = input('Please try again. Please input a three letter word ')
#print ('Your three letter word is: ', userInput)
#
##--------------------------------------------#
#"""Task Five: Putting code in logical order"""
##--------------------------------------------#
#
#print('\n****choice****')
#print('1. Display name')
#print('2. Display age')
#print('3. Display city')
#
#choice = int(input('What is your choice? '))
#while choice < 1 or choice > 3:
#    choice = int(input('What is your choice? '))
#if choice == 1:
#    print('Ms Wu')
#elif choice == 2:
#    print('5 years old')
#elif choice == 3:
#    print('London')   
#    
##--------------------------------------------------------#
#"""Task Six: Adding Exception and breaking out of loop"""
##--------------------------------------------------------#
#
####---Adding exception for wrong typ eof input---###

#print('\n------------------------')
#print('\n****choice****')
#print('1. Display name')
#print('2. Display age')
#print('3. Display city')
#
#choice = 0
##Need to initialise the variable in order for a whie loop to run
#
#while True:
##    choice = int(input('What is your choice? '))
#    try:
#        while choice < 1 or choice > 3:
#            choice = int(input('What is your choice? '))
#        break
#    except ValueError:
#        print('Please only input a number')
#        choice = 0
#if choice == 1:
#    print('Ms Wu')
#elif choice == 2:
#    print('5 years old')
#elif choice == 3:
#    print('London')   

#--------------------------------------------------#
"""Task Seven: Class-based user input validation"""
#--------------------------------------------------#

class Spam(object):
    
    def __init__(self, description, value):
#        if not description or value<=0:
#            raise ValueError
#can have a value error of an assertion whih must be met (raises an assertion error if not met)
        assert description != ""
        assert value >0
        self.description = description
        self.value = value
        
s1 = Spam('s',5)
s2 = Spam('t',-1)