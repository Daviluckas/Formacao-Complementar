def fatorial(num, show=False):
    
    """
    FATORIAL DE NÚMEROS
    n = O número a ser calculado
    show = mostrar ou não a conta
    return = O valor fatorial do número a ser mostrado.
    """
    f = 1 
    for cont in range(num, 0, -1):
        if show:
            print(f'{cont}', end = '')
            if cont > 1:
                print(f' x ', end = '')
            else:
                print(' = ', end = '')
        f *= cont
    return f

print('O fatorial de 5 é', end = ' ')

print(fatorial(5, show = True))
