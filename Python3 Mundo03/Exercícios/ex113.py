def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n 


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n 



num1 = leiaInt('Digite um valor inteiro: ')
num2 = leiaFloat('Digite um valor real: ')

print(f'O valor inteiro digitado foi {num1} e o valor real foi {num2}')
