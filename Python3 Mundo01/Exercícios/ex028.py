import random 
pc = str(print('O computador pensou em um número de 0 a 5, tente adivinhar qual é!'))
lista = (0, 1, 2, 3, 4, 5)
sorteio = random.choice(lista)
n = int(input('Digite o número que ele pensou: '))
if n == sorteio:
    print('PARABÉNS! Você acertou!')
else: 
    print('VOCÊ ERROU! Eu pensei no número {}. Tente novamente'.format(sorteio))
