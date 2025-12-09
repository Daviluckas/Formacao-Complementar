numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {c}: ')))
print(f'Você digitou os números {numeros}')
for posiçao, c in enumerate(numeros):
    if c == max(numeros):
        print(f'O maior número digitado foi o {max(numeros)} nas posições... {posiçao}')
    if c == min(numeros):  
        print(f'O menor número digitado foi o {min(numeros)} nas posições... {posiçao}')
numeros.sort()
print(f'Os números organizados na ordem crescente ficam assim {numeros}')
numeros.sort(reverse = True)
print(f'Os números na ordem decrescente ficam assim {numeros}')
print('')
