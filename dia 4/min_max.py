lista = [1,2,3,4,5,6,7]

print(f"el numero {min(lista)} es menor y el numero {max(lista)} es mayor")

nombres = ['David','Alex','Brayan']

print(min(nombres))

nombre = 'daVid'
print(min(nombre.lower())) 

dic = {'C1':45, 'C2':11}

print(min(dic.values()))

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)
print(rango)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
print(edad_minima)
ultimo_nombre = max(diccionario_edades.keys())
print(ultimo_nombre)