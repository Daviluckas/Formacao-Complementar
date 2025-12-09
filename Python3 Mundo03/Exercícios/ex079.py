#Método pensado inicialmente, porém não tinha a possibilidade de remover os números repetidos.
'''valores = []
v = valores.append(int(input(f'Digite um valor: ')))
for cont in valores:
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    while continuar == 'S':
        v = valores.append(int(input(f'Digite um valor: ')))
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(f'Você digitou os números {valores}')'''

#Método final pensando fora do FOR e utilizando WHILE.
valores = []
while True: 
    v = int(input('Digite um valor:' ))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado. ')
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    else:
        print('Ops... Valores repetidos não serão adicionados.')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        valores.sort()
        print(f'Os valores adicionados foram {valores}')
        break
