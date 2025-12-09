time = list()
gol = list()
dados = dict()
cont = 0
cont1 = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))  
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gol.clear()
    for c in range(0, partidas):
        gol.append(int(input(f'Quantos gols na partida {c + 1}? ')))

        cont += 1

    dados['gols'] = gol[:]
    dados['total'] = sum(gol)
    time.append(dados.copy())

    while True:
        continuar = str(input('Deseja continuar?[S/N] ')).upper()
        if continuar in 'SN':
            break
        print('OPS... Apenas S ou N')
    if continuar == 'N':
        break

print('-=' * 30)
print('cod ' , end = '')
for i in dados.keys():
    print(f'{i:<15}', end = '')

print('')

print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:>4}', end = ' ')

    for d in v.values():
        print(f'{str(d):<15}', end = '')

    print('')
print('-' * 40)

while True:
    procura = int(input('Deseja mostrar os dados de qual jogador? (Digite 999 se deseja parar) '))
    if procura == 999:
        break
    if procura >= len(time):
        print('OPS... Não existe jogador com com esse número nessa lista!')
    else:
        print(f'==> DADOS INDIVIDUAIS DO JOGADOR {time[procura]["nome"]}: ')
        for i, g in enumerate(time[procura]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')

    print('-' * 40)
