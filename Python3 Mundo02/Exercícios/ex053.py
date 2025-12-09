frase = str(input('Digite uma frase: ')).upper().strip()
separacao = frase.split()
juncao = ''.join(separacao)
contrario = ''
for c in range(len(juncao) - 1, -1, -1):
    contrario += juncao[c]
if contrario == juncao:
    print('Temos um PALÍNDROMO!')
else:
    print('Essa frase NÃO é um palíndromo!')