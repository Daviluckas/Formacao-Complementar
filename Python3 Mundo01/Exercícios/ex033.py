numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro: '))
numero3 = float(input('Digite mais um: '))
menor = numero1
if numero2<numero1 and numero2<numero3:
    menor = numero2
if numero3<numero1 and numero3<numero2:
    menor = numero3

maior = numero1 
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3> numero2:
    maior = numero3
print('O maior número é o {}!'.format(maior))
print('O menor número é o {}!'.format(menor))
