nombres =  ['Ana','Hugo','Valeria']
edades  = [65,29,42]
ciudades = ['lima','Madrid','Mexico']

combinados = list(zip(nombres,edades,ciudades))
for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} anos y vivie en {ciudad}")
    

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado2 = list((zip(paises,capitales)))

for pais, ciudad in combinado2: 
    print(f"La capital de {pais} es {ciudad}")


esp = ("uno","dos","tres","cuatro","cinco")
port = ("um","dois","três","quatro","cinco")
ing = ("one","two","three","four","five")

numeros = list(zip(esp,port,ing))

print(numeros)