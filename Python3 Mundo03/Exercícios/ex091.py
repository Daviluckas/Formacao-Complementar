from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6),}

ranking = list()

print('Valores sorteados: ')
for key, valor in jogo.items():
    print(f'{key} tirou {valor} no dado.')

    sleep(1)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)

print('-=' * 30)
print('--> RANKING DOS JOGADORES <--')

for itens, valor in enumerate(ranking):
    print(f'{itens + 1} lugar: {valor[0]} com {valor[1]}')

    sleep(1)
