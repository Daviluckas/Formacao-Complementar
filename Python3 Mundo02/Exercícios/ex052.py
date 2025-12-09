num = int(input('Digite um número para saber se ele é primo: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(end = '')
        total += 1
    else:
        print(end = '')
print('O número {} foi divisível {} vezes.'.format(num, total))
if total == 2:
    print('ELE É PRIMO!')
else: 
    print('ELE NÃO É PRIMO!')