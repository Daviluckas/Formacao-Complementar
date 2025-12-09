gol = list()
dados = dict()
cont = 0
cont1 = 0

dados['nome'] = str(input('Nome do jogador: '))  
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))

    cont += 1

dados['gols'] = gol[:]
dados['total'] = sum(gol)

print(dados)
print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} = {v}')

print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {cont} partidas ao todo.')

for p, g in enumerate(gol):
    print(f'--> Na partida {p} ele marcou {g} gols.')

print('-=' * 30)

print(f'Ao todo ele fez {dados["total"]} gols.')

print('')
