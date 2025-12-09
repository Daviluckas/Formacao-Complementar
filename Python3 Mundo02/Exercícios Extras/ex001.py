resultado = 0
print('---SUBTRAÇÃO---')
for conta in range(1, 4):
    print('---CONTA {}---'.format(conta))
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    resultado = n1 - n2 
    print('{} - {} = {}'.format(n1, n2, resultado))
