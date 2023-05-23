#obtener un nuevo valor de la lista segun su posicion
#siempre va con corchete la lista
lista =[1.2,"hola mundo desde la lista ",4,"posicion 4" ]
print(lista[2])
print("ultimo elemnto de la lista :",lista[-1])
print("el penultimo elemento", lista[-2])
#agregar un nuevo elemnto a la lista
lista.append("nuevo valor agregado con append")
lista.append(51)
lista.append(52)
lista.append(53)
#para extender la lista con el comando lista.extend  
lista_b=[54,55,56,1]
lista.extend(lista_b)
#agregar algo en la posicion [2] de la lista 
lista.insert(2,"objeto insertado en esta posicion")
lista.remove("posicion 4")#busca el elemento y lo borra de la lista
lista.pop()#elimina la ultima posicion
lista.reverse()# el lista.reverse es para dar vuelta la lista
lista_b.sort() #permite ordenar los elemento  de menor a mayor 
print("toda la lista")
print(lista)#imprime toda la lista