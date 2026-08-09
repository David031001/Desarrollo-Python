from random import * 

aleatorio = randint(1,50) # numeros aleatorios entre 1 y 50, tipo entero
print(aleatorio)

aleatorio = round(uniform(1,5),1) #numeros aleatorios entre 1 y 5, tipo decimal
print(aleatorio)

aleatorio = random() #numero aleatorios entre 0 y 1, fraccion
print(aleatorio)

colores = ['Azul','Rojo','Verde','Amarillo']
aleatorio = choice(colores) # elige un elemento aleatorio de la lista
print(aleatorio)

numeros = list(range(5,50,5))

shuffle(numeros) #mezcla los elementos, no se puede almacenar en una lista ni usar strings

print(numeros)
