diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)

alumno = {
    'Nombre': 'David',
    'Edad': 24,
    'Matricula': 32233
}

query = alumno['Nombre'] # forma de acceder a un elemento del diccionario
print(query)

diccionario2 = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}} #puedo meter listas y diccionarios dentro del un diccionario
print(diccionario2['c2'][1]) # para buscar elemento de una lista, dentro de un diccionario 
print(diccionario2['c3']['s1']) #para buscar lo que hay en un diccionario dentro de otro diccionario 

diccionario3 = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(diccionario3['c2'][1].upper())

#crear una clave en un diccionario ya existente

diccionario4 = {1:'a',2:'b'}

diccionario4[3] = 'c'

print(diccionario4)

#sobreescribir un valor

diccionario4[3] = 'nada'
print(diccionario4)

#como ver las claves de un diccionario 
print(diccionario4.keys())
#como ver los valores de un diccionario
print(diccionario4.values())
#como ver todo de un diccionario
print(diccionario4.items())

mi_dict = {'valores_1':{'v1':3,'v2':6},'puntos':{'points1':9,'points2':[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

mi_dic1 = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic1["ocupacion"] = "Editora"
mi_dic1["pais"] = "Colombia"
print(mi_dic1.items())