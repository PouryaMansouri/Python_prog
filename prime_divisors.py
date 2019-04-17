# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:38:12 2019

@author: Pourya Mansoury


"""
def isprime (number):
    
    # TODO : check number is prime or not
    prime = True
    if number == 1 :
        return  False
    else:
        for i in range(2,int(number/2)):
            if number%i==0:
               return False 
        return prime

   
num =input('What is the number? ')   # it can be anythings
divisors = list(filter(lambda x: num % x == 0, range(2,int(num**0.5))))
prime_divisors = list(filter(isprime,divisors))
print(prime_divisors)