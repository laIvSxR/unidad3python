import random, numpy as np
contador=0
acumulador=0
lista=[]
print(lista)
x =range(10)
#opcion"A"
for n in x :
    n_aleatorio=random.randint(0,1000)
    lista.append(n_aleatorio)
arreglo=np.array(lista)
print(n_aleatorio)
print(arreglo)
#la diferencia entre una lista y un arreglo son las comas. 
#si el modulo 2 del elemtno del arreglo es ==0 es pas si ==1 es impar
#corchete es para buscar en sub

largo_arreglo=len(arreglo)
for i in range(largo_arreglo):
     print(i)
    
     if arreglo[i] % 2 == 1:
        print(f"{arreglo[i]} impar")
        acumulador=acumulador+arreglo[i]
     if arreglo [i] % 2 == 0:
        print(f"{arreglo[i]} par")
        
        

print("resultado de la suma de los numero impares es :",acumulador)

        
        
        
        
     
    
