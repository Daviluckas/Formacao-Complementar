'''from math import factorial
numero = int(input('Digite um número para saber seu fatorial: '))
print(factorial(numero))'''

numero = int(input('Digite um número para saber seu fatorial: '))
c = numero 
fator = 1
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    fator *= c
    c -= 1
print('{}'.format(fator))
