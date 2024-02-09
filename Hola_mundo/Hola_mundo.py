#este es mi primer programa de Hola mundo----------------------------

#print('Hola mundo con python')

#Mis variables--------------------------------------------------------
entero = 10
flotente = 5.7 
cadena = "pepe"
bolean = True



#reglas para las variables-----------------------------------------
#iniciar las variables con pueden iniciar con guiones o letras 
mi_var = 12
_mi_var = 13

#No se puede iniciar con numeros el nombre de una variable, solo despues de la primer letra
# 3mi_var = 2 #Esto produce un error

# Las variables son sensibles a mayusculas y menusculas
Coco = 'verde'
coco = 'seco'
print()
print()

#No se pueden utilizar palabras reservadas para nombrar una Variable
#Class, if, for... se recominda usar notacion snake 'serpiente'
nombre_usuario = 'pancho' 

#Manejos de Cadena----------------------------------------------------------
saludo = 'Hola chito'
print (saludo)

# Agragar salto de linea con \n
saludo = 'hola \nchito'
print(saludo)

# Agregar un tabulador
saludo = 'hola \t chito'
print(saludo)

# Sub Cadenas---------------------------------------------------
sub_cadena = saludo[0:4]
print(sub_cadena)
sub_cadena = saludo[5:9]
print(sub_cadena)

# Metodos de cadenas en python Crear Mayusculas
saludo = 'muy bien gracias'
saludo_mayus = saludo.upper()
 
print(saludo_mayus)

# Comvertir en minusculas
saludo_minus = saludo_mayus.lower()
print (saludo_minus)

# Imprimir varios datos de string por concatenacion------------------------
mi_cadena1 = 'Practicas de '
mi_cadena2 = 'Python'

yo_practico = mi_cadena1 + mi_cadena2
print(mi_cadena1 + mi_cadena2 + ' que bien')
yo_practico = f'wao {mi_cadena1}{mi_cadena2}'
print(yo_practico)
print(f'super {mi_cadena1}{mi_cadena2}')

# Imprecion de cadenas multilineas
#
# Entradas de datos por consolas
#mensaje = #input('di tu nombre: ')
#print(f'mi nombre es: {mensaje}')

num_entrada1 = int(input('Dijite un numero para realizar una operacion aritmetrica: '))
num_entrada2 = int(input('Dijite otro numero para hacer la operacion: '))
print('la suma es: ', (num_entrada1 * num_entrada2) )