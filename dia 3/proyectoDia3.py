texto = input("Ingresa un texto: ")
letra1 = input("ingresa la primera letra :").lower()
letra2 = input("ingresa la segunda letra :").lower()
letra3 = input("ingresa la tercera letra :").lower()

textoM = texto.lower()

#letras = list(letra1+letra2+letra3)

#Parte 1
l1 = textoM.count(letra1)
l2 = textoM.count(letra2)
l3 = textoM.count(letra3)
print(f"la letra {letra1} aparece {l1} veces en el texto")
print(f"la letra {letra2} aparece {l2} veces en el texto")
print(f"la letra {letra3} aparece {l3} veces en el texto")

#parte 2
textoL = texto.split()
print(textoL)
print(f"El total de palabras en tu texto es de {len(textoL)}")

#parte 3
textoList = list(texto)
print(f"La primera letra de tu texto es: {texto[0]}")
print(f"La ultima letra de tu texto es: {texto[-1]}")

#parte 4 
textoInverso = texto[::-1]
print(textoInverso)

#parte 5

python = "python" in texto 
dic = {True: "si se encuentra la palabra python", False: "No se encuentra la palabra python"}
print(dic[python])


