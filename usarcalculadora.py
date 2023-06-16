from calculadora  import *




menu_activo=True
opcion_seleccionada=0
numero_1=0
numero_2=0
resultado=0

while menu_activo:
    print("1. sumar 2 numeros")
    print("2. restar 2 numeros")
    print("3. dividir 2 numeros")
    print("4. multiplicar 2 numeros")
    print("5. expotencial 2 numeros")
    print("6. salir")

    opcion_seleccionada=int(input("Seleccione una opcion\n"))

    if opcion_seleccionada == 1:
        print("selecciono opcion",opcion_seleccionada)
        numero_1 = int(input("ingrese el primer numero\n"))
        numero_2 = int(input("ingrese el segundo numero\n"))
        resultado = suma(numero_1,numero_2)
        print("el resultado es :",resultado)
    if opcion_seleccionada == 2:
        print("selecciono opcion",opcion_seleccionada)
        numero_1 = int(input("ingrese el primer numero\n"))
        numero_2 = int(input("ingrese el segundo numero\n"))
        resultado = resta(numero_1,numero_2)
        print("el resultado es :",resultado)

    if opcion_seleccionada == 3:
        print("selecciono opcion",opcion_seleccionada)
        numero_1 = int(input("ingrese el primer numero\n"))
        numero_2 = int(input("ingrese el segundo numero\n"))
        resultado = division(numero_1,numero_2)
        print("el resultado es :",resultado)

    if opcion_seleccionada == 4:
        print("selecciono opcion",opcion_seleccionada)
        numero_1 = int(input("ingrese el primer numero\n"))
        numero_2 = int(input("ingrese el segundo numero\n"))
        resultado = multiplicacion(numero_1,numero_2)
        print("el resultado es :",resultado)

    if opcion_seleccionada == 5:
        print("selecciono opcion",opcion_seleccionada)
        numero_1 = int(input("ingrese el primer numero\n"))
        numero_2 = int(input("ingrese el segundo numero\n"))
        resultado = elevar(numero_1,numero_2)
        print("el resultado es :",resultado)
    if opcion_seleccionada == 6:
        print("selecciono opcion",opcion_seleccionada)
        menu_activo=False
