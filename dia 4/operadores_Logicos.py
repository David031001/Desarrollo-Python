# Y  and
# O or
# No not 

mi_bool = (4 < 5) and (5 == 2 + 3)
print(mi_bool)

#con diferente tipo de dato
mi_bool = (4 < 5) and ("david" == "david")
print(mi_bool)

mi_bool = 10 == 10 or 3 == 2
print(mi_bool)

texto = "Esta frase es breve"

mi_bool = ("frase" in texto) or ("python" in texto)
print(mi_bool)


mi_bool = not ('a' == 'a') #not invierte el valor de la expresion, si es True lo convierte en False y viceversa
print(mi_bool)

