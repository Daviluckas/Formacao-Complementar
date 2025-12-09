dias = float(input('O veículo foi alugado por quantos dias? '))
km = float(input('Quantos quilômetros rodados?'))
kmr = km * 0.15
dia = 60 * dias
aluguel = dia + kmr
print('O total a ser pago pelo aluguel é R${}'.format(aluguel))
