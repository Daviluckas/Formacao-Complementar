multi = 1
num = int(input('Digite um número inteiro: '))
for c in range (1, num, 2):
    print(c)
    if c %2 !=0:
        multi *= c
print('O resultado da multiplicação de todos esses números é {}.'.format(multi))
