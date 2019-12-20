# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:43:01 2019

@author: 1-26-PB-L2-13
"""


file=open("devices.txt","a")
while True:
    newItem=input("Ingrese el registro: ")
    if newItem == "exit":
        print("All done!")
        break
    else:
        file.write(newItem + "\n")


file.close