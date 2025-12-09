h = float(input('Digite a altura da sua parede:'))
l = float(input('Agora digite a largura dessa parede:'))
a = h * l
print('O valor da área é: {:.2f}m'.format(a))
lt = a / 2
print('Para pintar essa área voçê necessitará de {:.3f}L de tinta.'.format(lt))
