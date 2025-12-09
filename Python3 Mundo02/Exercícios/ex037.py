import math
numero = int(input('Digite um número inteiro: '))
print('1 PARA BINÁRIO')
print('2 PARA OCTAL')
print('3 PARA HEXADECIMAL')

conversao = int(input('Escolha o número que corresponde a conversão desejada: '))

if conversao == 1:
    print('O número {}, convertido para binário é {}.'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('O número {} em octal é {}.'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('O número {} em hexadecimal é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida! Tente novamente.')