aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print('')

if aluno['media'] < 7.0:
    print(f'A média de {aluno["nome"]} é {aluno["media"]} . Sua situação é REPROVADO!')
elif aluno['media'] >= 7.0:
    print(f'A média de {aluno["nome"]} é {aluno["media"]} . Sua situação é APROVADO!')
print('')