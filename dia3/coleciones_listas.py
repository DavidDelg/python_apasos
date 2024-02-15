#creando listas
print('\n*** Coleccion tipo Lista ***')

nombres = ['karla', 'juan', 'laura']
#print(f'Lista de nombres: {nombres}')

lista_heterogenea =[100, True, 'ivone']

for nombre in nombres:
    print(nombre, end=' ')

numeros = [100, 200, 300, 400, 500]
#print(numeros[0]) #recupera el valor del indice 0
#print(numeros[3]) #recupero el valor del indice 3 que es 400
numeros[0] = 600
#print(numeros[0])

# Buscar elemento en una lista.
busca_element = 500

if busca_element in numeros:
    #Recupero el indice de un elemento.
    indice = numeros.index(busca_element)  
    print(f'\n--El elemento buscado es: {busca_element} con indice: {indice}')
else:
    print('\n--El elemento buscado NO EXISTE!!!')

# Recuperar una sublista. lista[indice_inicio, indice_final+1]
subLista_numeros = numeros[:3+1]
#si no se le ponen limites en los extremos se copia toda la lista
lista_duplicada = numeros[:] 

busca_por_indice = numeros[1]
insert_element_en_lista = numeros.insert(2, 10)# insertar elemento en el indice
añadir_elmentos_a_lista = numeros.append(7) #agregar elementos
eliminar_elemanto_de_lista = numeros.remove(7) # eliminar un elemento de la lista
del numeros[1] #elimina un elemento por el indice indicado
tamaño_de_lista = len(numeros) #metodos para listas.
#numeros[:] = [] # esta linea deja sin elementos la lista
print(f'''\n--Esta es la lista original: {numeros + lista_duplicada} 
      esta es la lista duplicada: {lista_duplicada}
      se agrego el dato: {añadir_elmentos_a_lista }
      ae inserto el dato: {insert_element_en_lista}
      se elimino el dato: {eliminar_elemanto_de_lista}
      buscando por indice es: {busca_por_indice}
      y su tamaño es: {tamaño_de_lista}''')


