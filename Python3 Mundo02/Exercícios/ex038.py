num = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))
if num > num2:
    print('O primeiro valor que é o número {} é o maior.'.format(num))
elif num2 > num:
    print('O segundo valor que é o número {} é o maior.'.format(num2))
else:
    print('Os valores {} e {}, são iguais.'.format(num, num2))
