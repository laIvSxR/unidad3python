


def calcular_iva(precio):
    iva = precio * 0.19
    total_con_iva = precio + iva
    return iva, total_con_iva

def calcular_descuento(precio, descuento):
    total_descuento = precio - descuento
    return descuento, total_descuento

def calcular_imc(peso, altura):
    estado = " no calculado"
    imc = peso / altura ** 2
    if  imc < 18.5 :
        estado =" bajo peso "
    elif imc >= 18.5 and imc <= 24.9:
        estado = "adecuado "
    elif imc >=25 and imc <= 29.9:
        estado = " sobre peso "
    elif imc >= 30 and imc <= 34.9:
        estado=" obesidad grado 1 "
    elif imc >= 35 and imc <= 39.9:
        estado= " obesidad grado 2 "
    elif imc >= 40 :
        estado = "obesidad grado 3 " 

    return estado + "imc = " + str (imc) 


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
