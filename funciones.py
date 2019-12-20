# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:15:15 2019

@author: 1-26-PB-L2-13
"""

#def hola(nombre):
#    print("Hola, ", nombre)
    
#nom = input("Ingrese su nombre: ")
#hola(nom)

#def holaTodos(nombre1, nombre2):
#    print("Hola",nombre1)
#    print("Hola",nombre2)
    
#holaTodos("Juan", "Luis")


#def direccion(calle, ciudad, codigopostal):
#    print("Tu dirección es:", calle, ". En la ciudad de", ciudad, ". y tienes el código postal:", codigopostal, ".")
    
#calle=input("Calle: ")
#ciudad=input("Ciudad: ")
#codigo=input("Código Postal: ")

#direccion(calle,ciudad,codigo)

#def subtra(a,b):
#    print(a-b)
    
#subtra(5,2)
#subtra(2,5)


#def subtra(a,b):
#    print(a-b)
    
#subtra(a=5, b=2)
#subtra(b=2, a=5)

#def multiplicar(a,b):
#    return a*b

#print(multiplicar(3,4))


#def multiplicar(a,b):
#    return

#print(multiplicar(3,4))

#def hiEverybody(myList):
#    for name in myList:
#        print("Hi,",name)
        
#hiEverybody(["Adam","John","Lucy"])


#def createList(n):
#    myList=[]
#    for i in range(n):
#        myList.append(i)
#    return myList

#print(createList(5))

#sumar=lambda x,y:x+y

#print(sumar(5,2))

#revertir = lambda cadena: cadena[::-1]

#print(revertir("Hola"))

#impar = lambda num: num%2 != 0

#print(impar(5))

#doblar = lambda num: num*2

#print(doblar(2))

#seq = ["data", "salt", "dairy","cat","dog"]

#print(list(filter(lambda word: word[0]=="d", seq)))

def isPrime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
               return False
    return True

for i in range(1,20):
    if isPrime(i+1):
        print(i+1, end=" ")
        

print(isPrime(1))



num = int(input('digite un numero: '))

if ((2** (num - 1)) % num) == 1 or num == 2:
    print('el numero es primo')
else:
    print('el numero No es primo')


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(1,20):
    if isPrime(i+1):
        print(i+1, end=" ")
        
        
num=input("Ingrese el numero:")
num=int(num)
list=[]
for i in range(num):
    list.append(i)

print(list)


def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
            
    
testData=[1900,2000,2016,1987]
testResults=[False,True,True,False]

for i in range(len(testData)):
    yr=testData[i]
    print(yr,"->",end="")
    result =isYearLeap(yr)
    if result==testResults[i]:
        print("OK")
    else:
        print("Failed")
        

def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
testData=[1900,2000,2016,1987]
testResults=[False,True,True,False]

for i in range(len(testData)):
    yr=testData[i]
    print(yr,"->",end="")
    result =isYearLeap(yr)
    if result==testResults[i]:
        print("OK")
    else:
        print("Failed")
        


def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    if year < 1500 or month < 1 or month >12:
        return None
    diameses=[31,28,30,31,30,31,30,31,30,31,30,31]
    if year <= 0 or month <= 0:
        return None
    else:
        if month == 2:
            if isYearLeap(year):
                return 29
            else:
                return diameses[month-1]
        else:
            return diameses[month-1]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
        
        
        
        

def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    if year < 1500 or month < 1 or month >12:
        return None
    days=[31,28,30,31,30,31,30,31,30,31,30,31]
    res = days[month-1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end=" ")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
        
           
        
def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    if year < 1500 or month < 1 or month >12:
        return None
    days=[31,28,30,31,30,31,30,31,30,31,30,31]
    res = days[month-1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(dayOfYear(2017, 1, 30))



    






