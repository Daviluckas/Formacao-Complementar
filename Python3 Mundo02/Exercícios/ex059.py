from time import sleep
num = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''---QUAL OPERAÇÃO DESEJA REALIZAR?---
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] ENCERRAR PROGRAMA''')
    opcao = int(input('O que deseja fazer? '))
    if opcao == 1:
        soma = num + num2
        print('SOMA = {:.2f} + {:.2f} = {:.2f}'.format(num, num2, soma))
    elif opcao == 2:
        multiplicacao = num * num2
        print('MULTIPLICAÇÃO = {:.2f} x {:.2f} = {:.2f}'.format(num, num2, multiplicacao))
    elif opcao == 3:
        if num > num2:
            maior = num
        else: 
            maior = num2
        print('Entre os números {} e {}, o maior é o número {}.'.format(num, num2, maior))
    elif opcao == 4:
        num = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    elif opcao == 5:
        print('Encerrando...')
        sleep(1)
    else:
        print('Essa opção é inválida. Tente com números de 1 a 5.')
print('PROGRAMA ENCERRADO')
