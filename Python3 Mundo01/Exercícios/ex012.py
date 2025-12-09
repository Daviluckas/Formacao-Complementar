p = float(input('Qual o preço do produto? R$'))
d = p * 5 / 100
p2 = p - d
print('Ao utilizar 5% de desconto na sua compra, seu produto ficará com o valor de R${:.2f}'.format(p2))
