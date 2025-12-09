print('APROVAÇÃO DE EMPRÉSTIMOS.')
print('-=-' * 9)

valor = float(input('Qual o valor da casa? R$'))

salario = float(input('Digite o valor do seu salário: R$'))

anos = int(input('Informe em quantos anos você pretende financiar essa casa: '))

salario2 = valor / (anos * 12)
porcentagem = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor, anos, salario2))

if salario2 > porcentagem:
    print('Infelizmente você não poderá finaciar essa casa pois seu saldo não é suficiente. \033[0;31m EMPRÉSTIMO NEGADO!\033[m')
else: 
    print('\033[0;32mEMPRÉSTIMO APROVADO!\033[m')
    