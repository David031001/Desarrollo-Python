#conversiones implicitas
print("conversiones implicitas")
num1 = 20
num2 = 30.3

num1 = num1 + num2

#la conversion es implicita por que al hacer la operacion automaticamente se convierte a float 

print(type(num1))
print(type(num2))

#explicita 
print("conversiones explicitas")

num3 = 5.8 
print(num3)
print(type(num3))

num4 = int(num3) # Aqui estamos conviertiendo manualmente un valor Floa a Int osea el 5.8 pasa a 5 
print(num4)
print(type(num4))

#edad = input("dime tu edad: ")

#print(type(edad))

#edad = int(edad)

#print(type(edad))

#nueva_edad = 1 + edad
#print(nueva_edad)

#ejercicio de prueba 

num_1 = "7.5"
num_2 = "10"

print(float(num_1)+ int(num_2))
