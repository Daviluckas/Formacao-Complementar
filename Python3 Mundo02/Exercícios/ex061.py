p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p1
contador = 1
while contador <= 10:
    print('{}'.format(termo), end = ' -> ')
    termo = termo + r
    contador += 1
print('FIM')