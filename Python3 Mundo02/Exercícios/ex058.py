import random 
pc = str(print('O computador pensou em um número de 0 a 10, tente adivinhar qual é!'))
print('-=-' * 23)
lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sorteio = random.choice(lista)
print(sorteio)
contagem = 0
n = int(input('Digite o número que ele pensou: '))
while n != sorteio:
        if n < sorteio:
            n = int(input('O número é maior do que o que você digitou... Tente de novo: '))
        elif n > sorteio:
           n = int(input('O número é menor do que o que você digitou... Tente de novo: '))
        contagem += 1
contagem += 1
print('Parabéns o computador pensou no número {}, e você acertou com {} tentativas!'.format(sorteio, contagem))
