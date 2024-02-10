num1, num2, num3, result = int(10), int(5), 7, 0

print('\n***Operaciones Aritmetricas***')
# Operaciones Aritmetricas
#print(f'suma:',num1+num2)
#print(f'resta:',num1-num2)
#print(f'multiplicacion:',num1*num2)
#print(f'divicion:',num1/num2)
#print(f'modulo:',num1&num3)
#print(f'exponente:',num1**3)

# Operadores de Asignacion
print('\n*** Operadores de Asignacion')
num1, num2, num3 = 3, 7, 9 #asignacion a multiples variables distintos valores
var1 = var2 = var3 = 5 # Asignacion de un mismo valor a multiples variables

# Operadores de asignacion conpuestas
print('\n***Operadores de Asignacion Compuestas***')
num1 += num2
num2 -= num1
#print(f'La operacion de num1 = num1 + num2 abrev num1 += num2 {num1}')
#print(f'La operacion de num2 = num1 - num2 abrev num1 -= num2 {num2}')

# Operadores de Comparacion (Relacionales)
#print(f'\n**** Operadores de Comparacion (Relacionales)')
result = num1 == num2 # Pregunta si es igual un valor al otro, Devuelve Valor booleano True False 
#print(f'La comparacion es: {result}')
result = num1 != num2 # Pregunta si un valor es diferente al otro, con un valor  booleano
#print(f'La comparacion es: {result}')

result = num1 > num2
#print(f'La comparacion de 10 mayor que -3 es: {result}')

result = num1 < num2
#print(f'La comparacion de 10 menor que -3 es: {result}')

result = num1 >= num2
#print(f'La comparacion 10 mayor o igual que -3 es: {result}')

result = num1 <= num2
#print(f'La comparacion 10 menor o igual que -3 es: {result}')

# Operadores Logicos and
print('\n *** Operador and ***')
comparacion1 = False
comparacion2 = False

if comparacion1 and comparacion2:
    print(f'la comparacion de {comparacion1} y {comparacion2}: es verdadero')
else:
    print(f'la comparacion de {comparacion1} y {comparacion2} es falsa \n')

# Operacion logico or
print('\n **** Operador Logico or ****')
if comparacion1 or comparacion2:
    print(f'La comparacion de {comparacion1} o {comparacion2} es verdadero')
else:
    print(f'La comparacion de {comparacion1} o {comparacion2} es falsa\n')

# Operador logico not
print(f'\n*** Operador Logico not ***')
if not  comparacion1:
    print(f'La comparacion de {comparacion1} ahora a combiado a: {comparacion1}')
else:
    print(f'La variables {comparacion1} no a cambiado')



