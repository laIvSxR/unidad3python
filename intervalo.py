import numpy as np
n=np.arange(0,1001,50);
print(n);
arreglo1=np.array([0,10,1])
#crear una copia superficial
arreglo2= arreglo1[:].copy()
print(arreglo2)
arreglo2[0] =100
print(arreglo2)
print(arreglo1)






