print('-' * 23)
print('BANCO SEU MUNDO PYTHON!')
print('-' * 23)
saque =  int(input('Quanto deseja sacar? R$'))
todo = saque
cedula = 50
cedulastotal = 0
while True:
    if todo >= cedula:
        todo -= cedula
        cedulastotal += 1
    else:
        print(f'Total de {cedulastotal} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cedulastotal = 0
        if todo == 0:
            break
