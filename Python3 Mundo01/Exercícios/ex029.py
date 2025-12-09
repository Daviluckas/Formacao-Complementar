velocidade = int(input('Qual foi a velocidade em quilômetros que você atingiu com seu veículo? '))
km = velocidade - 80 
multa = 7 * km
if velocidade > 80:
    print('Você estava andando além do limite de velocidade! A multa a ser paga é R${}'.format(multa))
else: 
    print('Você não precisará pagar multa, pois estava andando na velocidade permitida! Que nesse caso é 80Km/h.')
    