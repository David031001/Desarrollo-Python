from random import *


def lanzar_moneda():
    
    moneda = ['Cara', 'Cruz']
    lanzada = choice(moneda)
    
    return lanzada


def probar_suerte(moneda, lista):
    
    if moneda == "Cara":
        print("La lista se autodestruirá")
        lista.clear()
    elif moneda == "Cruz":
        print("la lista fue salvada")
    return lista


lista = [1,2,3,4,5]

print(probar_suerte(lanzar_moneda(), lista))
            