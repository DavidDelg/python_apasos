# Bucle wile
contador = 0
cadena_for ='Hola humanidad'
print('\n**** Bucle While ****')
valor_maximo = int(input('\ndigita el numero limite para el bucle while: '))
while contador < valor_maximo:
    contador +=1
    print(f'While vuelta {contador}')

print('\n**** Bucle For ****')
#cadena_for = 'Hola humanidad'
for letra in cadena_for:
    print(letra, end= ' ')

print()
for contador in range(1, valor_maximo+1):
    print(f'for vuelta', contador )

