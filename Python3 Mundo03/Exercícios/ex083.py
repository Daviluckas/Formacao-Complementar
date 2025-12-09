expressao = str(input('Digite uma expressão numérica: '))
aberto = []
fechado = []
for c in expressao:
    if c == '(':
        aberto.append(c)
    elif c == ')':
        fechado.append(c)
if len(aberto) == len(fechado):
    print('Essaa epressão é válida!')
else:
    print('Essa expressão é inválida!')
