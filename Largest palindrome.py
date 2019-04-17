# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:31:28 2019
title: Largest palindrome product
@author: Pourya Mansouri 

# TODO : fine  Largest palindrome between num1 and num2
"""


num1 = input('num1: ')
num2= input('num2: ')
list_num = []
while(num1>=799):
    number = num1 * num2
    string= str(number)
    if string==string[::-1]:
        list_num.append(number)
    num2 -= 1
    if num2 == 799:
        num1 -= 1
        num2 = 999
        
print(max(list_num))


