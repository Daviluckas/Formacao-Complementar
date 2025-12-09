produto = float(input('Qual é o preço do(s) produto(s) que você quer comprar? R$ '))
print('--------CONDIÇÃO DE PAGAMENTO--------')
print('[1] para pagar à vista com dinheiro;')
print('[2] para pagar à vista no cartão;')
print('[3] para parcelar em 2x no cartão;')
print('[4] para parcelar em 3x OU MAIS no cartão.')
opcao = int(input('Qual é a opção de pagamento desejada? '))

dez = produto * 10 / 100
vinte = produto * 20/ 100
cinco = produto * 5 / 10
vistac = produto - cinco
vistad = produto - dez
duasvezes = produto / 2
juros = produto + vinte

if opcao == 1:    
    print('Com o desconto de 10%, sua compra que era R${:.2f}, passa a custar R${:.2f}.'.format(produto, vistad))
elif opcao == 2:
    print('Com o desconto de 5%, sua compra que era R${:.2f}, passa a custar R${:.2f}'.format(produto, vistac))
elif opcao == 3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f}'.format(produto, duasvezes))
elif opcao == 4:
    vezes = int(input('Em quantas vezes deseja parcelar o produto?'))
    vezes2 = juros / vezes
    print('Sua compra será parcelada em {:.0f}x vezes de R${:.2f} COM JUROS.'.format(vezes, vezes2))
    print('Sua compra de R${:.2f} passa a custar R${}'.format(produto, juros))
else: 
    print('Opção inválida, tente novamente!')
    