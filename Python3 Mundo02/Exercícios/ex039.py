from datetime import date 
ano = int(input('Informe seu ano ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, anoatual))
subtracao = 18 - idade
soma = anoatual + subtracao
prazo = idade - 18
alistamento = anoatual - prazo
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(subtracao))
    print('Sue alistamento será em {}.'.format(soma))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(prazo))
    print('Seu alistamento ocorreu no ano de {}.'.format(alistamento))
elif idade == 18:
    print('Você tem que se alistar \033[0;31mimediatamente!\033[m')
    