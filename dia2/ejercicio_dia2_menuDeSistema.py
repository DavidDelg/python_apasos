#cree un menu de sistema de Administracion de cuentas
print('****\n Sistema de Administracion de Cuentas **** \n')
salir = False


while not salir:
    option = int(input('''          Menu:
                   1. Crear Cuenta
                   2. Eliminar Cuenta
                   3. Salir
                   Escoja una opcion:'''))
    if option==1:
        print('\nUsted creo una Cuenta!!!\n')
    elif option == 2:
        print('\nUsted a eliminado su cuenta!!!\n')
    elif option >= 4 or option <= 0:
        print('\nIngrese una opcion valida!!!\n') 

    if option == 3:
        print('\n*** Muchas Gracias por su preferencia ***\n')
        salir = True
    
    