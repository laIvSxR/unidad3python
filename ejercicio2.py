flag=True
numero=0
lista=[]
while flag:
    numero=int(input("ingrese un numero"));
    if numero==0:
        lista.append(numero);
        flag=False
    else :
         lista.append(numero);
lista.sort();
print(lista)
print("la lista tiene de largo :", len(lista))
print("la suma de los numero son:",sum(lista));
cantidad_elementos=len(lista)
suma_lista=(lista)
promedio=suma_lista/cantidad_elementos
print("el promedio de notas es :",promedio)


        
        
       
    




