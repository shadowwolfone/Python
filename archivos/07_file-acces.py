# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:25:56 2019

@author: 1-26-PB-L2-13
"""

file=open("devices.txt","r")
for item in file:
    item=item.strip()
    print(item)
file.close()


devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close
print(devices)