def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m quadrados.')


def linha():
    print('-' * 30)

linha()
print('   CONTROLE DE TERRENOS   ')
linha()

larg = float(input('LARGURA: ')) 
comp = float(input('COMPRIMENTO: '))
linha()
area(larg, comp)
linha()