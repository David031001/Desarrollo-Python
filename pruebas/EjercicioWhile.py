#crea un loop while que reste de uno en uno los numeros desde el 50 al 0(ambos numeros incluidos)
#con las siguientes condiciones adicialaes. 
# si el numero es divisible por 5 mostrar dichi numero en pantalla
#si el numero no es divisible por 5, continuar ejecutando el while sin mostrar el valor en pantalla


numeros = 50 

while numeros >= 0:
    if numeros%5 == 0:
        print(numeros)
    numeros -= 1
    
print('-----------------------------')
    
#crea un loop for a lo largo de la siguiente lista de numeros,
#imprimiendo en pantalla cada uno de sus elementos, e interrumpe
#el flujo en el momento que encuentres un valor negativo

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)