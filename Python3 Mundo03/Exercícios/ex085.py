#Utilizando mais de uma lista:

'''valores = []
pares = []
impares = [] 

for posicao in range(1,8):
    v = int(input(f'Digite o {posicao}º valor: '))
    valores.append(v)

    if v %2 == 0:
        pares.append(v)

    elif v %2 == 1:
        impares.append(v)

pares.sort()
impares.sort()
print('')

print(f'Os valores pares digitados foram {pares}.')
print(f'Os valores ímpares digitados foram {impares}.')'''


#Utilizando apenas uma lista:

valores = [[], []]

for posicao in range(1,8):
    v = int(input(f'Digite o {posicao}º valor: '))
    if v %2 == 0:
        valores[0].append(v)
    elif v %2 != 0:
        valores[1].append(v)
print('')
valores[0].sort()
valores[1].sort()

print(f'Os valores pares digitados foram {valores[0]}.')
print(f'Os valores ímpares digitados foram {valores[1]}.')
