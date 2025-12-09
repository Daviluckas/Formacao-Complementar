frase = str(input('Escreva uma frase:'))

vezes = str(frase.upper().count('A'))
p1 = (frase.find('a'))
p2 = (frase.rfind('a'))

print('A letra "A" aparece {} vezes nessa frase.'.format(vezes))
print('Ela aparece pela primeira vez na posição {}. '.format(p1))
print('Ela aparece pela última vez na posição {}.'.format(p2))