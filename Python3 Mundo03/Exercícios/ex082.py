valores = []
pares = []
impares = []

while True: 
    v = int(input('Digite um valor:' ))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    valores.append(v)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if v %2 == 0:
        pares.append(v)
    elif v %2 == 1:
        impares.append(v)
    if continuar == 'N':
        break 
print(f'A lista completa é {valores}')
print(f'A lista só de números pares é {pares}')
print(f'A lista só de números ímpares é {impares}')
