from datetime import date 
nascimento = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
print('Você tem {} anos de idade.'.format(idade))

#Mirim até 9, Infantil até 14, Junior até 19, Sênior até 20 e Master de 20 pra cima.

if idade < 10:
    print('Você é da categoria MIRIM na natação.')
elif idade < 15:
    print('Você é dacategoria INFANTIL na natação.')
elif idade < 20:
    print('Você é da categoria JUNIOR na natação.')
elif idade < 21:
    print('Você é da categoria SÊNIOR na natação.')
else:
    print('Você é da categoria MASTER na natação.')
