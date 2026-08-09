#descomponer un tuple sin funciones 

precios_cafe = [('Americano', 1.5), ('Expresso', 2.2), ('Moka', 1.9)]
"""
for cafe,precio in precios_cafe: 
    print(precio * 0.45 )
"""


#forma con  funcion 

def cafe_caro(lista_precios):
    
    precio_mayor = 0 
    cafe_caro = ''
    
    for cafe, precio in lista_precios:
        if precio > precio_mayor: 
            precio_mayor = precio 
            cafe_caro = cafe
        else: 
            pass
        
    return (cafe_caro, precio_mayor)

#print(cafe_caro(precios_cafe))

#Guardar resultado en 2 variables 

cafe, precio = cafe_caro(precios_cafe)

print(f"El cafe mas caro es {cafe} con un precio de {precio}")