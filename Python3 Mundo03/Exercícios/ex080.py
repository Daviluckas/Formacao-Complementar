valores = list()
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0:
        valores.append(v)
    elif v > valores[-1]:
        valores.append(v)
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos , v)
                break
            pos =+ 1
print(f'Os valores digitados e ordem foram {valores}.')
