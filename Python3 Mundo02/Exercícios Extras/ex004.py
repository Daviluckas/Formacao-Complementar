soma = 0 
print('NÚMEROS PARES DE 1 A 20')
for num in range(0, 21, 2):
    print(num)
    if num %2 == 0:
        soma = soma + num
print('A soma dos números pares é {}.'.format(soma))

