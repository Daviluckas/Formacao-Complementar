import random 
a1 = str(input('Informe o nome do priemiro aluno do grupo: '))
a2 = str(input('Agora o nome do segundo aluno: '))
a3 = str(input('Agora o nome do terceiro: '))
a4 = str(input('E por último, informe o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
ordem = random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))
