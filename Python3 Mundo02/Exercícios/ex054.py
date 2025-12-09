from datetime import date
anoatual = date.today().year
maioridade = 0 
menoridade = 0 
for pessoas in range(1, 8):
    ano = int(input('Digite o ano den nascimento da {}ª pessoa: '.format(pessoas)))
    idade = anoatual - ano
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('Temos {} pessoas maiores de idade.'.format(maioridade))
print('Temos {} pessoas menores de idade.'.format(menoridade))
