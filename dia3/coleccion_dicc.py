# Este es un diccionario colecion
print('*** Coleccion tipo diccionario ***')

gentes = [
    {'nombre': 'Regina', 'apellido': 'Flores', 'edad': 21}, 
    {'nombre': 'Alejandro', 'apellido': 'Reyes', 'edad':32},
    {'nombre': 'Alexandra', 'apellido': 'Mora', 'edad': 96}
]

for mi_person in gentes:    
    print(mi_person['nombre'], mi_person['apellido'], mi_person['edad'])


elimina_pers = gentes.pop(2)

print(f'Se elimino a {elimina_pers["nombre"]} {elimina_pers["apellido"]}')
print(gentes[0].get('nombre'), gentes[0].get('apellido'), gentes[0].get('edad'), gentes[0].keys() )