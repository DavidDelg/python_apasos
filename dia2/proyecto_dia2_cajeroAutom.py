#crear proyecto del dia 2 cajero automatico con:
#1.Consulta de salso 2.retirar 3.depositar 4.salir

print('\n **** Cajero Automatico de Ciudad Gotica ****\n')

salir = False
saldo = 500
deposito = 0
retiro = 0

def consultar_saldo():
    print(f'\nTu saldo en tu cuenta es: {saldo+deposito-retiro}\n')
    print('Consulta exitosa!!!')

def retirar_saldo():
    salir_retiro = False
    global saldo
    
    while not salir_retiro:
        retiro = int(input('Digite la cantidad que desea retirar o marque 0 para salir: '))
        if retiro > saldo:
            print('\nUsted no posee la cantidad indicada para retirar!!!\n')
        elif retiro <= -1:
            print('\nEl monto ingresado no es valido\n')
        elif retiro == 0:
            salir_retiro = True
        elif retiro < saldo and retiro > 0:
            saldo -= retiro
            print(f'\n Usted a retirado la Cantidad de: {retiro} \n')    
    exit

def depositar_saldo():
    global saldo
    salir_deposito =False
    while not salir_deposito:
        deposito = int(input('Ingrese la cantidad a depositar o marque cero 0 para salir:'))
        if deposito > 0:
            saldo += deposito
            print(f'\nUsted a depositado la cantidad de: {deposito} \n')
        elif deposito == 0:
            salir_deposito =True
        else:
            print('\nEl numero ingresado no es valido!!!')
    exit

while not salir:
    opcion = int(input('''\n                 Operaciones que puedes realizar:
                       1. Consultar Saldo
                       2. Retirar
                       3. Depositar 
                       4. Salir
                       Que gestion deseas realizar? '''))

    if opcion == 1:
        print('Consultando...')
        consultar_saldo()
    elif opcion == 2:
        print('Retirando...')
        retirar_saldo()
    elif opcion == 3:
        print('Depositando...')
        depositar_saldo()
    elif opcion == 4:
        print('\n**** Muchas Gracias por su preferencia ****\n')
        salir = True
    elif opcion <= 0 or opcion >=5:
        ('\nIngrese una opcion Valida!!!\n')




