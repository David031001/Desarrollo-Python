texto = "Este es el texto de david"

resultado = texto.upper() 
resultado = texto[2].upper()
resultado = texto.lower()
resultado = texto.split("t") # guarda los elementos en una lista, separados, si lo pongo split() usa espacios como separador

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])

print(e)

resultado = texto.find("s") # sino encuentra el caracter devuelve menos 1
resultado = texto.replace("s","x")
print(resultado)



lista_palabras = ["La","legibilidad","cuenta."]

union = " ".join(lista_palabras)
print(union)



frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

fragmento1 = frase[24:31]
fragmento1 = frase.replace(fragmento1,"fácil")
print(fragmento1.replace("mala","buena"))







