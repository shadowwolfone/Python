# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:15:25 2019

@author: 1-26-PB-L2-13
"""

import numpy as np

a=np.array([1,2,3])
print(a)

b=np.array([(1,2,3),(4,5,6)])
print(b[0,2])



import numpy as np
import sys

print("USO DE MEMORIA PYTHON")
S= range(1000)
print(sys.getsizeof(5)*len(S))
print ("\n"*1)
print("USO DE MEMORIA NUMPY")
D= np.arange(1000)
print(D.size*D.itemsize)





import numpy as np
import time
 
SIZE = 1000000
 
L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2=np.arange(SIZE)
print ("\n"*1)
print ("RESULTADO USANDO LISTAS/TUPLAS EN PYTHON")
start= time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
print ("\n"*2)
print ("RESULTADO USANDO NUMPY")
start=time.time()
result= A1+A2
print((time.time()-start)*1000)



import numpy as np

array=np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
print(array)




unos=np.ones((3,4))
print(unos)

ceros=np.zeros((3,4))
print(ceros)


a=np.array([(1,2,3)])
print(a.dtype)



a=np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)


a=np.array([(1,2,3,4),
            (5,6,7,8)])
print(a)
print("\n"*1)
print(a[1,0])



a=np.array([(1,2,3,4),
            (3,4,5,6)])
print(a[0:,1])




a=np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())



a=np.array([(1,2,3),(5,6,7)])
print("\n"*2)
print(np.sqrt(a))
print("\n"*2)
print(np.std(a))




x=np.array([(1,2,3),
            (3,4,5)])
y=np.array([(1,2,3),
            (3,4,5)])
print(x+y)
print("\n")
print(x-y)
print("\n")
print(x*y)
print("\n")
print(x/y)
print("\n")


a=np.array([[1,2],[3,4]])
b=np.array([[11,12],[13,14]])
print(np.dot(a,b))


import pandas as pd

a=pd.DataFrame([['a', 'b'], ['c', 'd']],
               index=['row 1', 'row 2'],
               columns=['col 1', 'col 2'])
a.to_excel("salida.xlsx")



data=np.array([['','Col1','Col2'],['Fila1',11,12],['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))







































