print('--------------TABUADA--------------')
print('=-' * 18)
n = 0
while True:
    n = int(input('Deseja ver a tabuada de qual valor? '))
    print('=-' * 18)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{c} x {n} = {n*c}')
print('O PROGRAMA SE ENCERROU. VOLTE SEMPRE!')
