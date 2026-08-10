nombre = input("cual es tu nombre")
ingresos = input("cuales fueron tus ingresos")

ingresos = float(ingresos)

comision = (ingresos * 13)/100 
comision = round(comision) # redondea a entero 

print(f"Hola {nombre} tus comisiones por tus ingresos de {ingresos} son de: ${comision} pesos")


 