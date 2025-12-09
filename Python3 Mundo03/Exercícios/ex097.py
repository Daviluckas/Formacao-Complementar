def titulo(texto):
    tamanho = len(texto) + 3
    print('~' * tamanho)
    print(f'{texto:^{tamanho}}')
    print('~' * tamanho)


titulo('   DAVI LUCAS   ')
titulo('   CURSO DE PYTHON3   ')
titulo('   CURSO EM VIDEO   ')
titulo('   BEIBE BEIBE DO BEIBE DO BIROLEIBE LEIBE   ')