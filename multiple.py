# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:50:28 2019
title: Largest palindrome product
@author: Pourya Mansouri 

# TODO :  smallest number divisible by each of the numbers
"""

from prime_divisors import isprime

def prime_divisors(num) : 
    #TODO: check divisor is prime or not
    divisors = list(filter(lambda x: num % x == 0, range(1,num+1)))
    return list(filter(isprime,divisors))


 
def cpd(num):
    # TODO: count prime divisors
    pd = prime_divisors(num)
    pd_dict= {}
    for i in pd:
        while (num%i==0):
            num /= i
            pd_dict[i] = pd_dict.get(i,0) + 1
    return pd_dict

number =  int(input('number : '))
num = 1

div1 = cpd(num)
for i in range(2,number):
    if num % i != 0:
        div2 = cpd(i)
        for d in div2:
            if div1.get(d,0) <  div2[d]:
                div1[d] =  div1.get(d,0)+(div2[d] - div1.get(d,0))

multi = 1
for item in div1:
    
    multi *= (item**div1[item])
print(multi)
        

