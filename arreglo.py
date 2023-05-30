import numpy as np
lista=[0,1,2,3,4,5,6,7,8,9,10]
#print(lista)
#type (lista)
a=np.array(lista)


suma=0
#recorrer el arreglo
for i in range(len(a)):
    suma=suma + (a[i]*a[i])
    print("el arreglo suma:",suma)
    #print(a[i])
    
#dimension del arreglo ndim
print(a.ndim)

#largo del arreglo
print(len(a))

#mostrar  intervalo
print(a[3::2])


#range en un array
c=[i for i in range(0,100)]
#print(c[::10])
print(a)




