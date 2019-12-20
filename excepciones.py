# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:02:16 2019

@author: 1-26-PB-L2-13
"""

import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print ("The square root of", x, "equals to", y)


value = 1
value /= 0


try:
    print("1")
    x=1/0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")


try:
    x=int(input("Ingrese un numero: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir para zero. lo siento")
except ValueError:
    print("Debes ingresar un valor entero")
except:
    print("halgo salio mal...")

print("FIN.")


try:
    y=1/0
except ArithmeticError:
    print("Arithmetic Problem")
except ZeroDivisionError:
    print("Zero Division!")
    
print("THE END.")


def badFun(n):
    try:
        return 1/0
    except ArithmeticError:
        print("Problema Aritmetico!")
    return None

badFun(0)
print("FIN.")

def badFun(n):
    return 1/0

try:
    badFun(0)
except ArithmeticError:
    print("What happend? An exception was raised")
    
print("THE END.")


















