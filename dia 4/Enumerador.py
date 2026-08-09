lista = ['a','b','c']

for indice, item in enumerate(lista):
    print(indice, item)


lista = ['a','b','c']

mis_tuples = list(enumerate(lista))
print(mis_tuples[1][1])


#Agragar tuples a una lista 

lista_indices = []

for i in enumerate("Python"):
    tupla = i
    lista_indices.append(tupla[0])
print(lista_indices)

'''
imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación,
que empiecen con M:
'''

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for nombre in enumerate(lista_nombres):
    if nombre[1][0] == 'M':
        print(nombre[0]) 
        
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
 
for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)