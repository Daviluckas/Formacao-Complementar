nota = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota + nota2) / 2
print('Sua média foi {:.1f}.'.format(media))

if media < 5.0:
    print('Você não atingiu a média necessária para a aprovação. \033[0;31mREPROVADO!\033[m')
elif media >= 5.0 and media < 7.0:
    print('Você está de \033[0;33mRECUPERAÇÃO!\033[m')
else:
    print('Parabéns! Você atingiu a média necessária. \033[0;32mAPROVADO!\033[m')
    