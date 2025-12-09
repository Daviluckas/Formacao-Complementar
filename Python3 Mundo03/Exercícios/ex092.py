from datetime import date

anoatual = date.today().year

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = anoatual - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (Digite 0 caso não tenha): '))

print('')

if dados['ctps'] != 0:
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contrato'] + 35) - anoatual
    
print('')

for k, v in dados.items():
    print(f'{k} tem o valor {v}')

print('')