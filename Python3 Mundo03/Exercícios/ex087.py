matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somapar = 0
for linha in range(0,3):
    for coluna in range(0, 3):
       matriz [linha] [coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-' * 60)
for linha in range(0, 3):
    for coluna in range (0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end = '')
        if matriz [linha] [coluna] %2 == 0:
            somapar += matriz [linha] [coluna]
    print()

soma = matriz[0][2] + matriz [1][2] + matriz[2][2]

print(f'A soma dos valores pares é {somapar}.')
print(f'O maior valor da 2ª linha é o {max(matriz[1])}.')
print(f'A soma dos valores da 3ª coluna é {soma}.')

#Diferentemente do exercício anterior que eu não consegui realizar. Esse eu consegui, e estou muito satisfeito.