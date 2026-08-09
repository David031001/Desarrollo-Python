#formas de crear los sets 

mi_set = set([1,2,3,4])
print(type(mi_set))
print(mi_set)
#forma 2
mi_set2 = {1,2,3}
print(type(mi_set2))
print(mi_set2)

mi_set3 = ((1,2,3,4,5))
print(len(mi_set3))

#union de sets

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)


s4 = {1,2,3}
s4.add(4)
s4.remove(3)
s4.discard(2)
eliminado = s4.pop() # aqui elimina un elemento aleatorio
#clear() vacia todo el set
print(eliminado)