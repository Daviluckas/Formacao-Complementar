print('-' * 28)
print('MERCADINHO SEU MUNDO PYTHON!')
print('-' * 28)
total = 0
mil = 0
maisbarato = 0
maisbaratoNome = 0
contador = 0
while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    total += preco
    contador += 1
    if contador == 1: 
        maisbarato = preco
        maisbaratoNome = nome
    else:
        if preco < maisbarato:
            maisbarato = preco
            maisbaratoNome = nome
    if preco > 1000:
        mil += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(f'O total a ser pago é R${total:.2f}')
print(f'{mil} Produtos custam mais de R$1000')
print(f'O produto com menor preço é {maisbaratoNome}, que custa R${maisbarato:.2f}')
