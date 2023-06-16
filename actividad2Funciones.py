


def calcular_iva(precio):
    iva = precio * 0.19
    total_con_iva = precio + iva
    return iva, total_con_iva

def calcular_descuento(precio, descuento):
    total_descuento = precio - descuento
    return descuento, total_descuento

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def mostrar_menu():
    print("Menú:")
    print("1. Calcular IVA ")
    print("2. Calcular Descuento ")
    print("3. Calcular IMC")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese el número de la opción que desea ingresar: "))

        if opcion == 1:
            precio = float(input("Ingrese el precio del producto: "))
            iva, total_con_iva = calcular_iva(precio)
            print("El valor del IVA es:", iva)
            print("El total del producto con IVA es:", total_con_iva)
        elif opcion == 2:
            precio = float(input("Ingrese el precio del producto: "))
            descuento = float(input("Ingrese el porcentaje de descuento: "))
            descuento_decimal = descuento / 100
            precio_descuento = precio - (precio * descuento_decimal)
            print("El precio con el descuento aplicado es:", precio_descuento)
        elif opcion == 3:
            peso = float(input("Ingrese su peso en kilogramos: "))
            altura = float(input("Ingrese su altura en metros: "))
            imc = calcular_imc(peso, altura)
            print("Su índice de masa corporal (IMC) es:", imc)
        elif opcion == 4:
            print("Usted a salido del programa. ")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

main()
