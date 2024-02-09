#Generador de ID unico
from random import randint


print('\n*** Generador de ID Unico ***')

nombre = str(input('Ingrese su nombre: '))
apellido = str(input('Ingrese su apellido: '))
anio_nacimiento = input('Ingrese su año de nacimiento YYYY: ')

letra_nombre = nombre[0:2].upper()
letra_apell = apellido[0:2].upper()
anio_nacimiento2 = int(anio_nacimiento[2:4])


# Generar numeros aleatorios
num_aleatorio = randint(0,9999)

print(f'Su ID unico es: {letra_nombre}{letra_apell}{anio_nacimiento2}{num_aleatorio}')
print('\n****Fin del programa****')
