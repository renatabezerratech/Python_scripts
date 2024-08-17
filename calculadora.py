valor1 = input('Entre com um valor inteiro positivo: ')
valor2 = input('Entre com um valor inteiro positivo: ')
x = int(valor1)
y = int(valor2)
op = input('Informe o operador (+, -, *, / ou **): ')
if op =='+':
 resultado = x + y
elif op =='-':
 resultado = x - y
elif op =='*':
 resultado = x * y
elif op =='/':
 resultado = x / y
elif op =='**':
 resultado = x ** y
else:
 resultado = None
if resultado == None:
 print(op, ': Operador inexistente!!')
else:
 print(x, op, y, '=', resultado)