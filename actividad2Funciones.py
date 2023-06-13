
import sys

def calcular_iva():
    precio = float(input("Ingrese el precio del producto: "))
    iva = precio * 0.19
    precio_total = precio - iva
    print(f"El precio total sin iva es: {precio_total}")
    print(f"el iva aplicado es  : {iva}")


def aplicar_descuento():
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))
    descuento_decimal = descuento / 100
    precio_descuento = precio - (precio * descuento_decimal)
    print(f"El precio con el descuento aplicado es: {precio_descuento:.2f}")


def calcular_imc():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Calcular IVA")
    print("2. Aplicar descuento")
    print("3. Calcular IMC")
    print("4. Salir")

    opcion = input("Ingresa el número de opción: ")
    return opcion

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            calcular_iva()
        elif opcion == '2':
            aplicar_descuento()
        elif opcion == '3':
            calcular_imc()
        elif opcion == '4':
            sys.exit()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.\n")

if __name__ == '__main__':
    main()

