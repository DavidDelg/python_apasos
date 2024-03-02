# Crear app de calculadora con funciones 

print('\n       *** Calculadora con funciones ***\n')

def mostrarMenu():
    print('================================================================')
    print('''       Estas son las operaciones que puedes realizar
          1 --> Suma.
          2 --> Resta.
          3 --> Multiplicacion.
          4 --> Divicion.
          5 --> Salir.''')
    print('================================================================')
    opcion = int(input('        Digite su opcion: '))
    return opcion

def perdir_valores():
    val1 = int(input('Dame le primer valor: '))
    val2 = int(input('Dame le segundo valor: '))
    return val1, val2

def ejecutar_operacion(opcion: int, salir: bool) -> None:
    """
    Esta funcion se encarga de realizar las operaciones de la calculadora.

    Args:
        opcion (int): Es la opcion elegida por el usuario.
        salir (bool): Es un valor que indica si el programa debe salir o no.

    Returns:
        None: No retorna nada.

    Raises:
        ValueError: Si la opcion elegida por el usuario es invalida.

    """
    if 1 <= opcion <= 4:
        # Si la opcion elegida por el usuario esta entre 1 y 4, se llama a la funcion perdir_valores
        # que pide los valores de los dos operandos
        operando1, operando2 = perdir_valores()

    if opcion == 1:
        # Si la opcion elegida es 1, se muestra en pantalla la suma de los dos operandos
        print(f'\nLa suma es: {operando1 + operando2}')

    elif opcion == 2:
        # Si la opcion elegida es 2, se muestra en pantalla la resta de los dos operandos
        print(f'\nLa resta es: {operando1 - operando2}')

    elif opcion == 3:
        # Si la opcion elegida es 3, se muestra en pantalla la multiplicacion de los dos operandos
        print(f'\nLa multiplicacion es: {operando1 * operando2}')

    elif opcion == 4:
        # Si la opcion elegida es 4, se muestra en pantalla la division de los dos operandos
        print(f'\nLa division es: {operando1 / operando2}')

    elif opcion == 5:
        # Si la opcion elegida es 5, se muestra un mensaje de agradecimiento y se establece el valor de salir a True
        print('\nGracias por usar la calculadora')
        salir = True

    else:
        # Si la opcion elegida por el usuario es invalida, se muestra un mensaje de error
        raise ValueError(f'Opcion invalida: {opcion}')

    return salir

# Codigo principal 
salir = False
while not salir:
    opcion = mostrarMenu()
    salir = ejecutar_operacion(opcion, salir)



