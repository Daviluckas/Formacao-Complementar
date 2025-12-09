soma = 0
maior = 0
velho = ''
mulher20 = 0
for pessoa in range(1, 5):
     print('{}ª PESSOA'.format(pessoa))
     n = str(input('Nome da pessoa: '))
     i = int(input('Idade da pessoa: '))
     s = str(input('Sexo da pessoa [M/F]: '))
     soma = soma + i
     if pessoa == 1 and s in 'Mm':
          maior = i
          velho = n
     if s in 'Mm' and i > maior:
          maior = i
          velho = n
     if s in 'Ff' and i < 20:
          mulher20 = mulher20 + 1
media = soma / 4
print('A média das idades é {:.1f}.'.format(media))
print('O homen mais velho tem {} anos e se chama {}.'.format(maior, velho))
print('{} Mulheres têm menos de 20 anos.'.format(mulher20))
     