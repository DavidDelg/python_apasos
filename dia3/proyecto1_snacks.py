# Primer proyecto del dia 3 
# simular una maquina de snacks compuesta por listas y diccionarios
# en donde muestre los snacks y se pueda comprar y regresar el vuelto de la compra.

import random
print('\n **** Maquina de Snack ****\n')

snacks_list = (
{'id':1, 'nombre':'Chips Ahoy', 'precio':500},
{'id':2, 'nombre':'Doritos', 'precio':700},
{'id':3, 'nombre':'Skittles', 'precio':200},
{'id':4, 'nombre':'M&Ms', 'precio':800},
{'id':5, 'nombre':'Twix', 'precio':400},
{'id':6, 'nombre':'Snickers', 'precio':400}, 
{'id':7, 'nombre':'Kit Kat', 'precio':300},
)

#Mostrar el inventario de snack
def mostrar_menu():
    print('\n **** Menu de Snacks ****\n')
    for snack in snacks_list:
        print(snack)

def seleccionar_snacks():
    mi_snack = int(input('''\n Ingrese el id del producto que desea comprar: '''))
    for snack in snacks_list:
        if snack['id'] == mi_snack:
            print(f'\n El snack seleccionado es: {snack['nombre'] } ')
            return mi_snack
        else:
            print(f'\n El snack seleccionado no existe intentalo de nuevo')
            seleccionar_snacks()
        
def comprar_snacks(mi_snack):
    compra = random.randint(0, 1000)
    if compra >= snacks_list[mi_snack-1]['precio']:

        print(f'Usted a comprado el producto {mi_snack}')
    else:
        comprar_snacks()
        print('Dinero insuficinte para realizar la compra intenta de nuevo')

opcion_while = False
while not opcion_while:
    opcion2 = int(input())
    mi_snack = seleccionar_snacks()
    comprar_snacks(mi_snack)