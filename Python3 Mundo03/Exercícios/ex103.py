def jogador(jog = '<DESCONHECIDO>' , gol = 0 ):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols ele fez? '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    jogador(gol = gols)
else:
    jogador(nome, gols)
