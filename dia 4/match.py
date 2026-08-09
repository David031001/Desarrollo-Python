#version de switch en python 

opcion = 'n-02'

match opcion:
    case 'n-02':
        print('Samsung')
    case 'n-03':
        print('Dell')
    case 'n-04':
        print('Sony')
    case _:
        print('No exixte el producto')
        
        
print("------------------")
    
    
cliente = {'nombre:': 'david',
           'edad:': 24,
           'ocupacion:': 'programador'}

pelicula = {'titulo:': 'chuky',
            'ficha_tecnica:': {'protagonista:': 'david vazquez',
                              'director:': 'alfonso cuaron'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e: 
        case {'nombre:': nombre,
               'edad:': edad,
               'ocupacion:': ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {'titulo:': titulo,
              'ficha_tecnica:': {'protagonista:': protagonista,
                                'director:': director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
            
        case _:
            print("No se que es esto")