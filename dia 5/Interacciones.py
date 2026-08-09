# interacciones entre funciones 

from random import shuffle

#Lista incial 

palitos = ['-','--', '---', '----']

#Mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return(lista)

#perdir intento 
def probar_suerte(): 
    intento = ''
    
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
        
    return int(intento)


#comprobar intento
def revisar(lista, intento):
    if lista[intento -1] == '-':
        print("a lavar los platos")
    else: 
        print("Esta vez te has salvado")
        
    print(f"Te ha tocado {lista[intento-1]}")
    
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
revisar(palitos_mezclados,seleccion)