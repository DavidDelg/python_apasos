num1, num2, num3, result = int(10), int(5), 7, 0

print('\n***Operaciones Aritmetricas***')
# Operaciones Aritmetricas
print(f'suma:',num1+num2)
print(f'resta:',num1-num2)
print(f'multiplicacion:',num1*num2)
print(f'divicion:',num1/num2)
print(f'modulo:',num1&num3)
print(f'exponente:',num1**3)

# Operadores de Asignacion
print('\n*** Operadores de Asignacion')
num1, num2, num3 = 3, 7, 9 #asignacion a multiples variables distintos valores
var1 = var2 = var3 = 5 # Asignacion de un mismo valor a multiples variables

# Operadores de asignacion conpuestas
print('\n***Operadores de Asignacion Compuestas***')
num1 += num2
num2 -= num1
print(f'La operacion de num1 = num1 + num2 abrev num1 += num2 {num1}')
print(f'La operacion de num2 = num1 - num2 abrev num1 -= num2 {num2}')

# Operadores de Comparacion (Relacionales)
print(f'\n**** Operadores de Comparacion (Relacionales)')
result = num1 == num2 # Pregunta si es igual un valor al otro, Devuelve Valor booleano True False 
print(f'La comparacion es: {result}')
result = num1 != num2 # Pregunta si un valor es diferente al otro, con un valor  booleano
print(f'La comparacion es: {result}')

result = num1 > num2
print(f'La comparacion de 10 mayor que -3 es: {result}')

result = num1 < num2
print(f'La comparacion de 10 menor que -3 es: {result}')

result = num1 >= num2
print(f'La comparacion 10 mayor o igual que -3 es: {result}')

result = num1 <= num2
print(f'La comparacion 10 menor o igual que -3 es: {result}')

# Operadores Logicos
print('*** Operador and ***')
comparacion1 = True
comparacion2 = True

