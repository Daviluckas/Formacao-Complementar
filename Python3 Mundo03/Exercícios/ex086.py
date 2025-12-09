matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0, 3):
        matriz [linha] [coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-' * 60)
for linha in range(0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5} ]', end = '')
    print()

'''Dessa vez não consegui realizar o exercício sozinho. 
Tive que fazer de acordo com a resolução. Apesar de ter me frustrado por não conseguir realiza-lo,
não me abalei, pois isso serviu de aprendizado para mim.'''
