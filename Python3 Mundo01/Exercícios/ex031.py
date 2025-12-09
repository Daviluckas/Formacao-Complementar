viagem = float(input('Qual a distância da sua viagem em Km?' ))
km = viagem * 0.50 
km2 = viagem * 0.45
if viagem <= 200:
    print('Sua passagem custa o valor de R${:.2f}, tendo em vista que a cada Km, é cobrado R$0.50.'.format(km))
else:
    print('Sua passagem custa o valor de R${:.2f}, tendo em vista que a cada Km, é cobrado R$0.45.'.format(km2))
    