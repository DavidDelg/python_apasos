# Este es el proyecto del dia numero 3 creando una maquina de snack
import random
print('\n **** Maquina de Snack ****\n')

snacks_list = (
{'id':1, 'nombre':'Chips Ahoy', 'precio':500},
{'id':2, 'nombre':'Doritos', 'precio':700},
{'id':3, 'nombre':'Skittles', 'precio':200},
{'id':4, 'nombre':'M&Ms', 'precio':800},
{'id':5, 'nombre':'Twix', 'precio':400},
{'id':6, 'nombre':'Snickers', 'precio':400}, 
{'id':7, 'nombre':'Kit Kat', 'precio':300} ,
{'id':8, 'nombre':'Sour Patch Kids', 'precio':600} , 
{'id':9, 'nombre':'Milky Way', 'precio':900}
 )

#Mostrar el inventario de snack
def mostrar_menu():
    print('\n **** Menu de Snacks ****\n')
    for snack in snacks_list:
        print(snack)

def seleccionar_snacks():
    # Pedir al usuario que ingrese el id del snack que desea
    id_snacks = int(input('Ingrese el Id del snack2: '))
    for snack in snacks_list:
        if snack['id'] == id_snacks:
            mi_snack = snack
            print('El snack es: %s' % snack["nombre"])
    # Si el id del snack ingresado es valido entoces devolver el id del snack
    if mi_snack:
        return mi_snack

    else:
        print('El id del snack no existe seleccione un id valido')
        return seleccionar_snacks()

def pagar(mi_snack): # Simular el pago del snack seleccionado
    pago = random.randint(0, 1000)
    print(f'El precio del snack seleccionado es de {mi_snack["precio"]} colones.')
    print(f'Ested pago con {pago} colones.')

    if pago >= mi_snack["precio"]:
        vuelto = pago - mi_snack["precio"]
        return vuelto
    else:
        print('El pago es insufiente. Intentalo de nuevo')
        return pagar(mi_snack)

def entrega_snack(mi_snack, vuelto):
    print(f'Su snack es: {mi_snack["nombre"]}')
    print(f'Su vuelto es: {vuelto} colones')

opcion = False
while not opcion:

    opcion_menu = int(input(f'''\n              ****  Bienvenido a la tinda de Snacks ****\n
                            1 --> Ver menu 
                            2 --> Salir
                            
                            '''))
    if opcion_menu == 1:
        mostrar_menu()

        print('''\n            1 --> Seleccionar producto
             2 --> Volver al menu''' )
        opcion_snack = int(input(                   ))

        if opcion_snack == 1:
            mi_snack = seleccionar_snacks()
            seleccionar_snacks()
            if mi_snack:
                vuelto = pagar(mi_snack)
                entrega_snack(mi_snack, vuelto)
        elif opcion_snack == 2:
            opcion = True
            print('\nMuchas gracias por su compra vuelve pronto...\n')
            

    elif opcion_menu == 2:
        print('\nMuchas gracias por su compra vuelve pronto...\n')
        opcion = True