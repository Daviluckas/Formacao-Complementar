# MANEIRA QUE EU FIZ A PRINCÍPIO.

tupla = ('Caderno', 12.50, 'Lápis', 0.75, 'Caneta', 1.25, 'Estojo', 9.90, 'Transferidor', 4.45, 'Régua', 2.0, 'Borracha', 2.75, 'Mochila', 145.99, 'Livro', 25.79 )
print('------------TABELA DE PREÇOS-------------')
print(tupla[0], end = '.........................R$ '), print(tupla[1])
print(tupla[2], end = '...........................R$ '), print(tupla[3])
print(tupla[4], end = '..........................R$ '), print(tupla[5])
print(tupla[6], end = '..........................R$ '), print(tupla[7])
print(tupla[8], end = '....................R$ '), print(tupla[9])
print(tupla[10], end = '...........................R$ '), print(tupla[11])
print(tupla[12], end = '........................R$ '), print(tupla[13])
print(tupla[14], end = '.........................R$ '), print(tupla[15])
print(tupla[16], end = '...........................R$ '), print(tupla[17])
print('-' * 41)

#MANEIRA COMPACTA, DO GUSTAVO GUANABARA!

'''tupla = ('Caderno', 12.50, 'Lápis', 0.75, 'Caneta', 1.25, 'Estojo', 9.90, 'Transferidor', 4.45, 'Régua', 2.0, 'Borracha', 2.75, 'Mochila', 145.99, 'Livro', 25.79 )
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
for pos in range(0, len(tupla)):
    if pos %2 == 0:
        print(f'{tupla[pos]:.<30}', end ='')
    else:
        print(f'R${tupla[pos]:>7}')'''
    