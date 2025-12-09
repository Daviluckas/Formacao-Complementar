soma = 0 
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma dos valores ímpares múltiplos de 3, de 1 a 500 é {}.'. format(soma))
 