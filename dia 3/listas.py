#las listas en python pueden tener varios tipos de datos 

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
resultado = mi_lista + mi_lista2

resultado.append('g') #append agrega

eliminado = resultado.pop(0) #pop elimina, si pongo el pop() asi, elimina el ultimo elemento

print(resultado)
print(eliminado)

lista_ordenada = [4,3,20,13]
lista_ordenada.sort() # ojo, sort() no se puede almacenar el un variable
lista_ordenada.reverse() # reverse hace lo mismo que sort() pero ala inversa


lista_ordenada.clear() #Elimina todo el contenido e la lista


print(lista_ordenada)


lista_numeros = [1,2,3,4,5,6,7,8,9] 
lista_numeros.append(10)
print(lista_numeros)

eliminado = lista_numeros.pop(5) 

print(lista_numeros)
print(eliminado)