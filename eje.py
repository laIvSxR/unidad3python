nombres = []
for i in range(3):
    nombre = input("Ingrese un nombre: ");
    nombres.append(nombre);
nombre_mayor = max(nombres, key=len);
print("El nombre con mayor cantidad de caracteres es:", nombre_mayor);