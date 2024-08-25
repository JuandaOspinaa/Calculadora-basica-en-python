#Calculadora Basica

def suma (a,b):
    return a + b
def resta (a,b):
    return a - b
def multi (a,b):
    return a * b
def div (a,b):
    if b == 0:
        raise ZeroDivisionError('No se puede dividir por cero.')
    return a/b
def mod(a,b):
    if b == 0:
        raise ZeroDivisionError('No se puede dividir por cero,')
    return a % b
    
    

try:
    num1 = int(input('ingrese el primer digito: \n '))
    num2 = int(input('ingrese el segundo digito: \n'))
    operacion = input('''Escoja la operacion:
                      1. Suma
                      2. Resta
                      3. Multiplicacion
                      4.Division
                      5.Modulo \n''')
    
    if operacion == '1':
        resultado = suma(num1,num2)
    elif operacion == '2':
        resultado = resta(num1,num2)
    elif operacion == '3':
        resultado = multi(num1,num2)
    elif operacion == '4':
        resultado = div(num1,num2)
    elif operacion == '5':
        resultado = mod(num1,num2)
    else:
        print('operacion no valida.')
        
    print(f'el resultado de la operacion es: {resultado}')
    print('Fin del programa.')
    
except ValueError as e:
    print(f'Error: {e}')
    print('Por favor, ingrese un valor valido.')
    