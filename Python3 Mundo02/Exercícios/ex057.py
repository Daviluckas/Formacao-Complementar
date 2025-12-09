sexo = str(input('Qual é o seu sexo? [M/F] ')).upper()
while sexo not in 'MF':
    sexo = str(input('Por favor digite algo válido: ')).upper()
print('Sexo {} registrado.'.format(sexo))
