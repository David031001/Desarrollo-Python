from random import *

nombre = input("Hola cual es tu nombre: ")
print(f"{nombre},elige un numero del 1 al 100 tienes solo 8 intentos para adivinar el numero")

intentos = 8 

num_secreto = randint(1,101)

while intentos > 0:
   num_jugador = int(input("Elige un numero entre el 1 al 100: "))
   print(f"Intentos Restantes {intentos}")
   intentos -=1
   match num_jugador:
       case num if num < 1 or num > 100:
           print(f"El numero {num} no esta permitido")
       case num if num < num_secreto:
           print(f"Su respuesta es incorrecta, ha elegido un numero menor al numero correcto")
       case num if num > num_secreto:
           print(f"Su respuesta es incorrecta, ha elegido un numero mayor al numero correcto")
       case num if num == num_secreto:
           print(f"Su respues es correcta: {num} = {num_secreto}")
