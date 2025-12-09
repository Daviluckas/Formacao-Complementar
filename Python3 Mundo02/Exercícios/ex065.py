continuar = 'S'
soma = 0 
contagem = 0
media = 0
maior = 0 
menor = 0
while continuar == 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar != 'N':
        print('Se deseja parar digite N')
    soma += n 
    contagem += 1
    media = soma / contagem
    if contagem == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('A média desses números é {:.2f}.'.format(media))
print('O maior valor é o número {} e o menor valor é o número {}.'.format(maior, menor))