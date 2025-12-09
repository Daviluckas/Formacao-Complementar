par = 0 
impar = 0 
numero = int(input('Digite um número: '))
for num in range(0, numero):
    if num %2 == 0:
        par = par + 1
    if num %2 != 0:
        impar = impar + 1
print('Há {} números pares e {} números ímpares até o número {}.'.format(par, impar, numero))
