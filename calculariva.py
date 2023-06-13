def calcular_iva():
    precio = float(input("Ingrese el precio del producto: "))
    iva = precio * 0.19
    precio_total = precio + iva
    print(f"El precio total con IVA es: {precio_total:.2f}")
