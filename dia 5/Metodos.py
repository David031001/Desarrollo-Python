dic = {'clave1': 100, 'Clave2': 500}

a = dic.popitem() 

print(a)
print(dic)  

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#  ".lstrip(",:%_#")

print(texto)


txt = ",,,,,jsrte.....manzana"

x = txt.lstrip(",jsrte.") # elimina todo lo que coincide con esos caracteres por eso el resultado es manzana


print(x)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 

frutas.insert(3, "naranja") # inserta un obtjeto en una lista antes de alguno indice, insert(indice, objeto)

print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv) 
#el metodo isdisjoint verifica si los conjuntos son disjuntos, si tienen elementos en comun
#no son disjutos por lo que mandaria False y si no tienen nada en comun mandaria True 

print(conjuntos_aislados)