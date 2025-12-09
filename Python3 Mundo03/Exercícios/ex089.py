lista = []

while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))

    media = (nota1 + nota2) / 2

    lista.append([aluno, [nota1, nota2], media])
 
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
  
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('-' * 30)
print(f'{'Nº.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 30)
for indice, a in enumerate(lista):
    print(f'{indice:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    qual = int(input('Deseja ver as notas de qual aluno? (999 para interromper): '))
    if qual == 999:
        print('ENCERRANDO...')
        break
    if qual <= len(lista) - 1:
        print(f'AS notas de {lista[qual][0]} são {lista[qual][1]}')
print('-=-= ATÉ MAIS! =-=-')
