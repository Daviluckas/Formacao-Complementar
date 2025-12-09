from random import choice
print('=-' * 10)
print('JOGO DO PAR OU ÍMPAR')
print('=-' * 10)
jogador = 0
valor = 0
soma = 0
contador = 0
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sorteio = choice(lista)
while True:
    valor = int(input('Digite um valor: '))
    soma = valor + sorteio 
    ip = str(input('Deseja escolher PAR ou ÍMPAR? [P/I] ')).upper()
    if ip == 'P' and (soma %2 == 0):
        print(f'Você escolheu {valor} e computador escolheu {sorteio}. A soma é {soma} e é PAR')
        print('PARABÉNS! VOCÊ GANHOU!')
        print('Vamos continuar...')
        contador += 1
        print('-=' * 30)
    elif ip == 'I' and (soma %2 != 0):
        print(f'Você escolheu {valor} e computador escolheu {sorteio}. A soma é {soma} e é ÍMPAR')
        print('PARABÉNS! VOCÊ GANHOU!')
        print('Vamos continuar...')
        contador += 1
        print('-=' * 30)
    elif ip != 'P' and (soma %2 == 0):
        print(f'Você escolheu {valor} e computador escolheu {sorteio}. A soma é {soma} e é PAR')
        print('-=' * 30)
        print(f'GAME OVER! VOCÊ VENCEU {contador} VEZES.')
        break
    elif ip != 'P' and (soma %2 != 0):
        print(f'Você escolheu {valor} e computador escolheu {sorteio}. A soma é {soma} e é ÍMPAR')
        print('-=' * 30)
        print(f'GAME OVER! VOCÊ VENCEU {contador} VEZES.')
        break
