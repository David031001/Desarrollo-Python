

lista_numeros = [234,343,342,2000] 

def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma = suma + n 
    return suma     

resultado = suma_menores(lista_numeros)
print(resultado)
  