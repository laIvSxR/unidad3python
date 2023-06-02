#import numpy as np
#c = [i for i in range(50,101,10)]
#print(c)
#import numpy as np
#c =np.array ([i for i in range(50,101,10)]);
#c=c*3
#print(c);
import numpy as np
c =np.array ([i*3 for i in range(50,101,10)]);
print(c);
#tradicional
import numpy as np 
matriz = np.array([[0,1,2],[3,4,5]])
for f in range (2):
    for c in range(3):
        print(matriz[f][c]);
print(matriz[1,1]);
#crear una lista
matriz = np.array([[0,1,2],[3,4,5]])
print(matriz)
#crear una lista
import numpy as np 
lista=[[1,2,3,],[4,5,6]]
matriz=np.array(lista)
print (matriz)

import numpy as np 
matriz=np.zeros((3,3))
print(matriz)

import numpy as np 
matriz=np.ones((3,3,))
print(matriz)

import numpy as np 
matriz=np.diag([1,1,1,])
print(matriz)

import numpy as np 
lista=[[1,2,3],[4,5,6]]
matriz=np.array(lista)
print(matriz.sum())

import numpy as np
lista=[[1,2,3],[4,5,6]]
matriz=np.array(lista)
print("suma elemntos0:", matriz[0:], sum())
print("suma elemntos 1:", matriz[1:], sum())
import numpy as np
matriz= np.array([[0,1,2],[3,4,5]])
matriz.ndia
import numpy as np
matriz= np.array([[0,1,2],[3,4,5]])
matriz.shape
import numpy as np
matriz= np.array([[0,1,2],[3,4,5]])
matriz.size

import numpy as np 
m1=np.array([[1,2,3],[4,5,6]])
m2=np.array([[10,20,30],[40,50,60]])
np.concatenate((m1,m2),axi5=5)














