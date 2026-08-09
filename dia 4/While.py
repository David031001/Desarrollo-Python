#ejemplo 1
monedas = 5

while monedas > 0: 
    print(f"tengo {monedas} monedas")
    monedas = monedas -1
    #forma mas sencilla
    #monedas -= 1 
else: print("No tengo mas dinero")

#pass reserva un lugar para terminar el loop 
#break interrumpe la iteracion 
#continue salta la iteracion actual y pasa ala siguiente 


print('--------------')

#ejemplo 2 
respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres seguir? (s?n):')
else: 
    print('Gracias por participar')


print('--------------')

 
#ejemplo de break con for

nombre = input('tu nombre: ')

for letra in nombre:
    if letra == 'r':
        break
    print(letra)


numero = 50 

