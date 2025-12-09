n = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um:' ))
n4 = int(input('Digite outro: '))
valores = (n, n2, n3, n4)
print(f'Os valores digitados foram {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O número 3 apareceu na {valores.index(3)+1} posição.')
else: 
    print('O número 3 não foi digitado nenhuma vez')
print(f'Os números pares digitados foram', end = ' ')
for par in valores:
    if par %2 == 0:
        print(par, end  = ' ')
else:
    print(0)
    