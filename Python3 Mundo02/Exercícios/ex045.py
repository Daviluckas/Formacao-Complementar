from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('Vamos jogar jokenpô?')
print('-' * 25)
print('''---SELEÇÃO DE OBJETOS---
[0] para escolher PEDRA
[1] para escolher PAPEL
[2] para escolher TESOURA''')
print('-' * 25)

selecao = int(input('Escolha:'))
print('=-=' * 9)
print('Você escolheu {}.'.format(lista[selecao]))
print('O computador escolheu {}.'.format(lista[comp]))
print('PROCESSANDO...')
sleep(2)

if comp ==  0:
    if selecao == 0:
        print('\033[33mEMPATE\033[m')
    elif selecao == 1:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif selecao == 2: 
        print('\033[31mO COMPUTADOR GANHOU!\033[m')
    else: 
        print('VOCÊ SÓ PODE JOGAR OS NÚMEROS DE 0 A 2! Tente novamente.')
if comp == 1:
    if selecao == 0:
        print('\033[31mO COMPUTADOR GANHOU!\033[m')
    elif selecao == 1:
        print('\033[33mEMPATE\033[m')
    elif selecao == 2: 
        print('\033[32mVOCÊ GANHOU!\033[m')
    else: 
        print('VOCÊ SÓ PODE JOGAR OS NÚMEROS DE 0 A 2! Tente novamente.')
if comp == 2:
    if selecao == 0:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif selecao == 1:
        print('\033[31mO COMPUTADOR GANHOU!\033[m')
    elif selecao == 2: 
        print('\033[33mEMPATE\033[m')
    else:
        print('VOCÊ SÓ PODE JOGAR OS NÚMEROS DE 0 A 2! Tente novamente.')
