from random import * 

# lanzar los dados al azar 

def lanzar_dados():
    res1 = randint(1,6)
    res2 = randint(1,6)
    return res1, res2

# Evaluar jugada 

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10: 
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2))