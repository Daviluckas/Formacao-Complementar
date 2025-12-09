lista = []
pessoas = {}
 
contador = 0
soma = 0 
media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Apenas M ou F')

    pessoas['idade'] = int(input('Idade: '))

    soma += pessoas['idade']
    
    lista.append(pessoas.copy())

    contador += 1

    media = soma / contador

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Apenas S ou N')
    if continuar == 'N':  
        break

print('-=' * 30)
print(f'-> O grupo tem {contador} pessoas.')
print(f'-> A média de idade é {media:.2f} anos.')
print(f'-> As mulheres cadastradas foram', end = ' ')

for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end = ' ')

print('')
print('-> Pessoas que estão acima da média', end = ' ')
for p in lista:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}', end = ' ')
        print('')