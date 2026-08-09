"""  
Este codigo le pasa una lista ala funcion reducir lista, y lo que la funcion
con esa lista es reducirla eliminando los duplicados y el valor mas alto,
despues la funcion promedio toma como parametro esa funcion que ya devuelve una
lista reducida, suma sus valores y saca el promedio/
"""

def reducir_lista(lista):
    
    lista_nueva = []
    for n in lista:
        if n not in lista_nueva:
            lista_nueva.append(n)
            
    mayor = max(lista_nueva)
    lista_nueva.remove(mayor)
    
    return lista_nueva

def promedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio


lista_numeros = [1,2,15,7,2]
print(reducir_lista(lista_numeros))
print(promedio(reducir_lista(lista_numeros)))
      
        
    