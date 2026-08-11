lista = ['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) + 1               #index() es un metodo que sirve para buscar el indice de un elemento en una lista
    print(f'Letra {numero_letra}: {letra}')

print('--------------------------------')  

lista2 = ['Pablo','Laura','Fede','Luis','Julia']

for nombre in lista2:
    if nombre.startswith('L'):        #startswith() es un metodo que sirve para buscar si un string empieza con una letra o palabra en especifico
        print(nombre)

print('--------------------------------')  

numeros = [1,2,3,4,5]
suma_numeros = 0 

for numero in numeros:
    suma_numeros = suma_numeros + numero
print(suma_numeros)

print('--------------------------------')  

for letra2 in 'Python':
    print(letra2)


print('--------------------------------')  
# como iterar un lista dentro de otra lista 

for a,b in [[1,2],[3,4],[5,6]]:
    print(a+b)
    
    
print('--------------------------------')  

dic = {'Clave1':'a','Clave2':'b', 'Clave3': 'c'}

for a,b in dic.items():    #items() es un metodo que sirve para recorrer un diccionario y obtener la clave y el valor de cada elemento
    print(a,b)
    
    
#Ejercicio de practica 
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0 

for numero in lista_numeros:
    if numero%2 == 0: 
        suma_pares = suma_pares + numero 
    elif numero%2 == 1:
        suma_impares = suma_impares + numero 

print(suma_pares)
print(suma_impares)