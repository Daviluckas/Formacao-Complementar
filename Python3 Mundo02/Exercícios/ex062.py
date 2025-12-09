p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p1
contador = 1
total = 0
continuar = 10
while continuar != 0:
    total = total + continuar
    while contador <= total:
        print('{}'.format(termo), end = ' -> ')
        termo = termo + r
        contador += 1
    print('Programa Pausado...')
    continuar = int(input('Deseja continuar? Digite o número de termos que deseja: '))
print('PROGRAMA ENCERRADO COM {} TERMOS.'.format(total))
