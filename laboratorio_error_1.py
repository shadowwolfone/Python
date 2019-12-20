# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:11:49 2019

@author: 1-26-PB-L2-13
"""

def readint(prompt, min, max):
    comp = prompt * 1
    return (comp)


a = int(input("Enter a number from -10 to 10: "))

try:
    while a < -10 and a > 10:
        v = readint(a, -10, 10)
        print("the value is not within permitted range (-10..10) ")
        a = int(input("Enter a number from -10 to 10: "))
except ValueError:
        print ("Wrong input")
        
        
print("The number is:", v)





def fun(x,a,b):
    y=list(range(a,b,1))  

    for i in range(0,len(y)):
         r=y[i]
         if r==x: 
             a=1;
             break
         else:
             a=0;
    return a         

try:
    x=int(input("Ingrese el numero a buscar: "))
    a=int(input("Ingrese el limite inferior: "))
    b=int(input("Ingrese el limite superior: "))
    f=fun(x,a,b)
    if f==1:
        print("the value is: ",x)
    else:
        print("the value is not within permitted range ")
except ValueError:
    print("wrong input ")
