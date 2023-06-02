import numpy as np
arreglo = np.empty(3)
for i in range(3):
    a = int(input("Ingrese los numeros:\n "))
    arreglo[i] = a
copia_arreglo = np.copy(arreglo)
mayor = np.max(copia_arreglo)
menor = np.min(copia_arreglo)
suma = np.sum(copia_arreglo)
promedio = np.mean(copia_arreglo)
print("Elementos del arreglo:")
for a in copia_arreglo:
    print(a)
print("numero mayor:", mayor)
print(" numero menor:", menor)
print("Suma de los numero:", suma)
print("Promedio de los numeros:", promedio)