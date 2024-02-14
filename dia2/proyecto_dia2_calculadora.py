#Proyecto 2 del dia dos creando calculadora 
print('\n**** Calculadora de consola en python ****\n')

salir = False
result = 0
#opcion = 0

def sumar():
    global result
    salir_suma = False
    while not salir_suma:
         num_suma = int(input('\nIngresa un numero para sumar o ingrese 00 para salir al menu principal: '))
         if num_suma != 00:
            num_suma2 =int(input('\nIngrese el segundo numero a sumar: '))
            result = num_suma + num_suma2
            print(f'El resultado de la suma es: {result}')
         if num_suma == 00:
             salir_suma = True
    print('\nSalindo de las sumas...\n')
    exit
def restar():
    global result 
    salir_resta = False
    while not salir_resta:
        num_resta = int(input('\nIngrese un numero para restar o ingrese 00 para salir al menu principal:'))
        if num_resta != 00:
            num_resta2 = int(input('\nIngrese el segundo numero a restar: '))
            result = num_resta - num_resta2
            print(f'El resltado de su resta es: {result}')
        if num_resta == 00:
            salir_resta = True
    print('\nSaliendo de la resta...\n')
    exit
            
def multiplicar():
    global result
    salir_multi = False
    while not salir_multi:
        num_multi = int(input('\nIngrese un numero a multiplicar o ingrese 00 para salir: '))
        if num_multi != 00:
            num_multi2 = int(input('\nIngrese el segundo numero a multiplicar: '))
            result = num_multi * num_multi2
            print(f'El resultado de la multiplicacion es: {result}')
        if num_multi == 00:
            salir_multi = True
    print('\nSaliendo de la multiplicacion...\n')
    exit

def dividir():
    global result
    salir_div = False
    while not salir_div:
        num_div  = int(input('\nIngrese un numero a dividir o ingrese 00 para salir al menu princiapal: '))
        if num_div != 00:
            num_div2 = int(input('Ingrese el segundo numero a dividir: '))
            result = num_div / num_div2
            print(f'El resultado de la divicion es: {result}')
        if num_div == 00:
            salir_div = True
    print('\nSaliendo de la divicion...\n')
    exit

while not salir:
    
    print(f'''\n Operaciones que puedes realizar:
          1. Suma
          2.Resta
          3. Multiplicacion
          4. Divicion
          5. Salir
          ''')
    opcion = int(input('Escoje una opcion: '))
    if opcion == 5:
        salir = True
    elif opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        dividir()




