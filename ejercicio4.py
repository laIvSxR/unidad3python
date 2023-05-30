import random
while True:
    def listaAleatorios(n):
        lista = []
        for i in range(n):
            lista.insert(i, random.randrange(0, 100, 2))
        return lista

    print("Ingrese cuantos numeros aleatorios desea obtener")
    n = int(input())

    aleatorios = listaAleatorios(n)
    print(aleatorios)