valores = []
contagem = 0
while True: 
    v = int(input('Digite um valor:' ))
    contagem += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    valores.append(v)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        valores.sort(reverse = True)
        print(f'Você digitou {contagem} valores.')
        print(f'Os valores em ordem decrescente são {valores}')
        if 5 in valores:
            print('O valor 5 faz parte dessa lista')
        else:
            print('O valor 5 NÃO faz parte dessa lista.')
        break
    