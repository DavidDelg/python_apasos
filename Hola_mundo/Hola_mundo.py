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
