# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:50:06 2019

@author: 1-26-PB-L2-13
"""

def fib(num):
    a, b = 0,1
    while a < num:
        print(a, end=' ')
        """ c=a+b
        a=b
        b=c"""
        a, b = b, a+b
#    print('Termino')