
'''
def chequear_3_cifras(lista):
    
    lista_3_cifras = []
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass 
    resultado = chequear_3_cifras([443 ,55,434])
print(resultado)
'''

lista_numeros = [2,3,4,5,6]

def todos_positivos(lista_numeros):
    
    for n in lista_numeros:
        if n < 0:
            return False
    return True

resultado2 = todos_positivos(lista_numeros)

print(resultado2)
    
 
lista_numeros = [234,343,342,2000] 

def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma = suma + n 
    return suma     

resultado = suma_menores(lista_numeros)
print(resultado)
  
  
#formas de contar un numero apartir de una coindicion, en este caso que contar los numeros que sean pares  

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

def cantidad_pares(lista_numeros):
    cuenta = 0
    for n in lista_numeros:
        if n%2 == 0:
            cuenta += 1
    return cuenta

resultado = cantidad_pares(lista_numeros)
print(resultado)


lista_numeros = [1,2,3,4,5,6,7,8,9,10]

def cantidad(lista_numeros):
    cantidad_pares = len([n for n in lista_numeros if n%2 == 0])
    print(cantidad_pares)

cantidad(lista_numeros)
