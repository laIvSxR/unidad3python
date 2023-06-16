from ejerciciostipopr1 import *
import numpy as np
menu=True
opcion=0
precio=0
numero_producto=""
nombre_producto=0
#codigo_ejemplo="123456-a22 nombre producto"
todo_los_productos=[]


while menu:
    print("Menu")
    print("1. Grabar producto")
    print("2. Buscar producto")
    print("3. Imprimir reporte")
    print("4. Salir")
    opcion=int(input("Selecciona una opción:\n"))  


    if opcion== 1:
        print("selecciono la opcion",opcion)
        for n in range(3):
          numero_producto=str(input("ingrese el numero del producto: "))
          nombre_producto=str(input("ingrese el nombre del producto :"))
          precio =int(input("ingrese el precio del producto: "))
          resultado_validacion = validar_informacion(numero_producto,nombre_producto,precio)
          if resultado_validacion==True:
               un_producto=[numero_producto,nombre_producto,precio]
               todo_los_productos.append(un_producto)
        print(todo_los_productos)


    if opcion== 2:
          print("selecciono la opcion",opcion)

    if opcion== 3:
           print("selecciono la opcion",opcion)

    if opcion== 4:
           print("A salido del programa")
           menu=False

