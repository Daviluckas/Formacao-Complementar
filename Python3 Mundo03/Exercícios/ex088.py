from random import shuffle
from time import sleep
print('-=' * 10)
print(f'{'-----MEGA SENA-----'}')
print('-=' * 10)
print('')

numeros = list(range(0,61))

jogos = int(input('Quantos jogos você deseja sortear? [LIMITE 10]'))
for c in range(1 ,jogos + 1):
    print(f'Jogo número {c}', end = ' ')
    sleep(1)
    shuffle(numeros)
    print(numeros[:6])
    del(numeros[:6])
print('')
print('Jogue com moderação!')
