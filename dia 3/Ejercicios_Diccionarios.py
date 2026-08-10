
carro = {
        "Marca": "Toyota",
        "Modelo": "Corolla",
        "Año": 2020,
        "Color": "Rojo",
}

marca = carro["Marca"]
modelo = carro["Modelo"]
año = carro["Año"]
color = carro["Color"]

print(f"El carro es un {año} {marca} {modelo} de color {color}")


autos = {
    "auto1": {"Color":"Azul", "Marca":"Mazda", "Modelo":"CX-5", "Año":2021},
    "auto2": {"Color":"Negro", "Marca":"Chevrolet", "Modelo":"Aveo", "Año":2020}
}   

auto = autos["auto1"]["Marca"]

print(auto)