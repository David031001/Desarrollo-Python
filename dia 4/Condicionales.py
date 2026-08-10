  

if 10 > 91:
    print('Es correcto') 
else:
    print('No es correcto')
    
    
mascota = 'perro'

if mascota == 'gato': 
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else: 
    print('No se que animal tienes') 

#if anidado

edad = 16 
calificacion = 9
if edad < 18: 
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Estas Aprobado')
    else: 
        print('No estas aprobado')
else: 
    print('eres adulto')


#Ejercicio de practica
    
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else: 
    print(f"{num1} y {num2} son iguales")
    
# la diferencia entre if y elif es que elif solo se ejecuta si el if no se cumple, mientras que if se ejecuta siempre que la condicion sea verdadera.