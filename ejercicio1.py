numero_ingresado=int(input("ingrese un numero"));
resultado=0
x=range(1,11)
lista_tabla=[]
for n  in x :
    resultado=n*numero_ingresado
    lista_tabla.append(resultado)
   # print(f"{n}*{numero_ingresado}={resultado}");
print("la tabla de multiplicar del numero:", numero_ingresado);
print(lista_tabla)