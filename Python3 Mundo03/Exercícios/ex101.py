from datetime import date
anoatual = date.today().year

def idade(a = 0):
    a = anoatual - nasc
    if a < 16:
        return f'Com {a} anos ainda NÃO VOTA!'
    elif 16 <= a < 18 or a > 65:
        return f'Com {a} anos o voto é OPCIONAL!'
    else:
        return f'Com {a} anos o voto é OBRIGTATÓRIO!'


nasc = int(input('Digite o seu ano de nascimento: '))
print(idade(nasc))
