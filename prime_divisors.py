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
    elif number == 2:
        return True
    else:
        for i in range(2,int(number/2)+1):
            if number%i==0:
               return False 
        return prime

if __name__ == "__main__":
    num =int(input('What is the number? '))  # it can be anythings
    divisors = list(filter(lambda x: num % x == 0, range(1,num+1)))
    prime_divisors = list(filter(isprime,divisors))
    print(prime_divisors)