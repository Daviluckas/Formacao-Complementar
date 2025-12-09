n = 0
s = 0
contagem = 0
while True:
    n = int(input('Digite um número [999 se desejar parar]: '))
    if n == 999:
        break
    contagem += 1
    s += n
print(f'A soma dos {contagem} valores digitados é {s}.')
