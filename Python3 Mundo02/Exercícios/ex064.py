num = 0
contagem = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para o programa!]:'))
    if num != 999:
        soma += num
        contagem += 1
print('Você digitou {} números, a soma entre eles é {}.'.format(contagem, soma))
