print('BRASILEIRÃO ASSAÍ 2023')
print('-=-' * 57)
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print(f'Os cinco primeiros colocados da tabela são {times[0:5]}')
print('-=-' * 57)
print(f'Os quatro últimos colocados databela são {times[-4:]}')
print('-=-' * 57)
print(f'Ordem alfabética {sorted(times)} \n')
print('-=-' * 57)
seutime = str(input('Digite o seu time para saber a posição dele: '))
if seutime in times:
    print(f'O {seutime} está na {times.index(seutime)+1}ª posição.')
else:
    print('Seu time não está nessa lista.')
