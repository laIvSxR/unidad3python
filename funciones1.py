#funcion sin periemtro y sin retorno 
def saludo ():
    print("saludando a mis estudiantes ")
#se ejecuta solo si la utilizo
saludo()
#sin argumentos(parametro) y con retorno
def sumar():
    num1=3
    num2=5
    return(num1+num2)
print("la suma es :", sumar())
#funcion con argumento(parametro) y sin retonro
def sumar(a,b):
    sumar = a + b 
    print(f"la suma de los argumentos es :{sumar}")
num1= int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))
sumar(num1,num2)

#funciones con argumentos y con retorno
def suma(a,b):
    sumar = a + b 
    return(suma)
num1= int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))
print(f"el resultado de la suma es :",sumar(num1,num2))

#otras funciones
def varios_valores(*args):
    for arg in args:
        print(arg)
varios_valores(4.5,"buen dia",[1,2,3,4,5])

def mostrar_valores():
    return("buen dia",15,[10,20,30])
mostrar_valores()


def resta(a,b):
    return a - b 
resta(30, 10)

