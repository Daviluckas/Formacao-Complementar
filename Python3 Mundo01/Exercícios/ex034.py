salario = float(input('Qual o valor do seu salário? R$ ')) 
aumento1 = salario * 10 / 100
aumento2 = salario * 15 / 100
valorfinal = aumento1 + salario 
valorfinal2 = aumento2 + salario
if salario > 1250:
    print('Parabéns! Você recebeu um aumento de 10% no seu salário. Agora você receberá R${}.'.format(valorfinal))
else:
    print('Parabéns! Você recebeu um aumento de 15% no seu salário. Agora você receberá R${}.'.format(valorfinal2))
