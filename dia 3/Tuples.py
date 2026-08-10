mi_tuple = (1,2,3,4)
print(type(mi_tuple))

mi_tuple2 = (1,2,(10,20),3)
print(mi_tuple2[2][0]) #buscar que hay en un tuple dentro de un tuple. 

mi_tuple2 = list(mi_tuple2) #converit tuple a lista
print(type(mi_tuple2))
print(mi_tuple2)

mi_tuple2 = tuple(mi_tuple2) #converit lista a tuple
print(type(mi_tuple2))

t = (1,2,3)

x,y,z = t # puedo asignar asi siempre y cuando el mismo nuevo de variables sea el mismo que de elemento en una tuple

print(x,y,z) # tambien funciona con listas y diccionarios 

u = (1,2,3,1)

print(len(u))
print(u.count(1)) # cuenta cantidad de apariciones de un elemento

# las listas se pueden modificar, pero los tuples no se pueden modificar
