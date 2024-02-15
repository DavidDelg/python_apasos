print('**** Coleccion tipo Tupla ****')
nombres = ('Karla', 'Juan', 'Laura')
t_difent_valor = (100, True, 'Yo')
t_otra = 5,
t_numeros = (1, 2, 3, 4, 5, 6, 7)

for nombre in nombres:
    pass # print(nombres) #muestra los datos que hay en la tupla

busca_por_indice = t_numeros[3]

print(f'''\nEsta es la tupla de nombres: {nombres}
Esta es la tupla de difirentes valores: {t_difent_valor}
El numero buscado por indice es: {busca_por_indice}

Esta es la tupla de numeros: {t_numeros}
\n''')