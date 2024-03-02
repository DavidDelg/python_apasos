# Creando funciones con argumentos

def crear_persona(nombre ='', apellido='', edad=0):


    print(f'Nombre: {nombre}, apellido: {apellido}, edad: {edad}')

# si quitamos un argumento da error porque espera los tres
#se puede quitar solo si se le da valores a las variables 
#desde los arg de la funcion
crear_persona('David', 'Reyes', 22)

#llamar a la funcion argumentos por nombre
crear_persona(nombre = 'david', apellido = 'John')

#regresar una tupla de valores desde una funcion
def obtener_nombre(nombre ='', apellido='', edad=0):
    print('\nEsta funcion regresa varios valores (tupla)')

    return nombre.upper(), apellido.upper(), edad

nombre, apellido, edad = obtener_nombre('David', 'Reyes', 22)
print(f'Nombre: {nombre}, apellido: {apellido}, edad: {edad}')