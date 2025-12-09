from time import sleep

def ajuda(com):
    titulo(f'Acessando o manual do comando {com}...')
    help(com)

    sleep(1.5)

def titulo(msg):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)

    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHTON')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')
