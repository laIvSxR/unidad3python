#actividad 1 
def resta(a,b):
    return a - b 
resta(30, 10)
print(resta(30, 10))
#2
def resta (a ,b):
    return a - b 
resta(b=30 , a = 10)
print(resta(b=30 , a = 10))
#3
def funcion():
    return "bienvenido a python"
frase = funcion()
print(frase)
#4
def resta(a=None, b=None):
    if a == None or b == None:
        print("error , falta parametro a la funcion ")
        return
    return a - b 
resta()
#5
def calculo(precios, descuento):
    return precios - (precios*descuento/100)
datos=[10000,1]
print("el monto final es :",calculo(*datos))
#6
def saludo(nombre , mensaje='python'):
    print(mensaje,nombre)
saludo(mensaje="buen dia",nombre="pedro")


