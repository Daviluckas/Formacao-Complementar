def notas(*n, sit = False):
    """
    Função para analisar notas e situações de vários alunos.
    n = uma ou mais notas dos alunos.
    sit = valor opcional, indica a situação em que o aluno se encontra.
    return = dicionário com várias informações sobre a turma.
    
    """


    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r ['média'] >= 7:
            r['situação'] = 'BOA'

        elif r ['média'] >= 5:
            r['situação'] = 'RÁZOAVEL'
        else:
            r['situação'] = 'RUIM'

    return r

resposta = notas(9, 10, 5.5, 2.5, 8.5, sit = True)
print(resposta)
