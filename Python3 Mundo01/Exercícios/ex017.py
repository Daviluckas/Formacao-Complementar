ct1 = float(input('Digite o comprimento do cateto oposto: '))
ct2 = float(input('Digite o comprimento do cateto adjacente:'))
h = (ct1**2 + ct2**2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(h))
