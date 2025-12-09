tupla = ('Comer', 'Brincar' 'Estudar', 'Python', 'Ensino', 'Programador', 'Mundo', 'Viagem', 'Planeta', 'Aprender', 'Correr', 'Linguagem')
for itens in tupla:
    print(f'\nNa palavra {itens} temos as vogais:', end = ' ')
    for letras in itens:
        if letras in 'aeiou':
            print(letras, end = ' ')
print('')