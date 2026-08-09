
lista = [letra for letra in 'python']
print(lista)

lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista) 

pies  = [10,20,30,40,50]
metros = [p/3.281 for p in pies]

print(metros)

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [((p-32)*(5/9)) for p in temperatura_fahrenheit]

print(grados_celsius)