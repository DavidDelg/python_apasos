# If Else
print('\n***Sentencias if else****')

dia_con_lluvia = False
dia_nublado = True
if dia_con_lluvia:
    print('Llevar paraguas esta lloviendo')
else:
    print('hay sol')

#elif 
print('\n*** Sentencia elif ***')
if dia_con_lluvia:
    print('Llevar paraguas hoy')
elif dia_nublado:
    print('Llevar impermiables hoy')
else:
    print('Dejar todo hay un  solaso hoy')

#Ejercicios Verifica si un numero ingresado por el usuario es positivo
num1 = int(input('\nVerifica si un numero es positivo o negativo: '))
if num1 > 0:
    print(f'El numero {num1} ingresado es positivo')
elif num1 < 0:
    print(f'El numero {num1} ingresado es negativo')
else:
    print(f'El numero ingresado es cero') 


