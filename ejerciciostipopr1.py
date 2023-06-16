
def grabar(lista_producto):
    print("funcion grabar")

def buscar(numero_parte):
    print("buscando")

def imprimir (): 
    print("imprimiendo")

def validar_informacion(numero_producto,nombre_producto,precio):
     precio_valido=False
     nombre_valido=False
     numero_valido=False
     if numero_producto.index("-") == 6 and numero_producto.index("-") ==10:
     
        
        numero_valido=True
     else:
        print("numero no valido")
       
     if len(nombre_producto)==6:
        nombre_valido=True
       
     else:
        print("nombre no valido")
     if precio > 0 :
        
        precio_valido=True
     else :
        print("precio no valido")
     if precio_valido == True and numero_valido == True and nombre_valido == True:
        return True
     else:
        return False
     

