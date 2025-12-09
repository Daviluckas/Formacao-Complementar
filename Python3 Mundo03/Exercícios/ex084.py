#O programa está 100% funcional, o único problema é não conseguir mostrar de quem são o maior e menor peso.

'''people = []
dados = []
peso = []
contador = 0

while True:
    dados.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    people.append(dados[:])
    dados.clear()
    
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    contador += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()

    if continuar == 'N':
        peso.sort()
        print(f'Ao todo {contador} pessoas foram cadastradas. ')
        print(f'O maior peso é {peso[-1]}Kg. ')
        print(f'O menor peso é {peso[0]}Kg. ')
        break
'''

#Solução encontrada após assistir a resolução do exercício. 
#Basicamente adicionei a parte de mostrar o nome da pessoa correspondente ao seu peso, assim como Guanabara fez. 
#Porém NÃO copiei seu código todo. Apenas adicionei o que precisava.

people = []
dados = []
contador = 0
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(people) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados
        if dados[1] < menor:
            menor = dados[1]
    people.append(dados[:])
    dados.clear()
    
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    contador += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print(f'O total de essoas cadastradas foi {contador}.')

print(f'O maior peso foi {maior}kg. Peso de ', end = '')
for p in people:
    if p[1] == maior:
        print(f'[{p[0]}]', end = '')
print('')

print(f'O maior peso foi {menor}Kg. Peso de ', end = '')
for p in people:
    if p[1] == menor:
        print(f'[{p[0]}]', end = '')
print('')
