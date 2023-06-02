#ejercicio1
import numpy as np
arreglo = np.random.randint(0, 101, size=(3, 3))
matriz = np.array(arreglo)

#ejercicio 2
arreglo = np.random.randint(0, 101, size=(3, 3))
matriz = np.array(arreglo)
print("proimedio", matriz.sum()/matriz.size)
print("suma", matriz.sum())
print("maximo", matriz.max())
print("minimo",matriz.min())
#ejercicio3
arreglo = np.zeros((3, 3))
np.fill_diagonal(arreglo, [1, 2, 3])
matriz = np.array(arreglo)
print(matriz)


