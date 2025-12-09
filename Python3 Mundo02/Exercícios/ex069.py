print('---CADASTROS---')
homen = 0
mulher = 0
maioridade = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    while sexo not in 'MF':
          sexo = str(input('Sexo [M/F]: ')).upper()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homen += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(f'No cadastro realizado, {maioridade} pessoas tem 18 anos ou mais;')
print(f'Temos a presença de {homen} pessoas do sexo masculino;')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
