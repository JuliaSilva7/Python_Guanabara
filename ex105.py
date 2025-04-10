def notas(*n, sit=False):
    """ A função notas permite a inserção de notas usuário a partir da quantidade que o usuário desejar através do parâmetro n. O parâmetro opcional sit, se for iniciado como True, permite ver o status do aluno de acordo com a sua média."""
    notas_dict = dict()
    notas_dict['total'] = len(n)
    notas_dict['maior'] = max(n)
    notas_dict['menor'] = min(n)
    notas_dict['media'] = sum(n) / len(n)
    if sit:
        if notas_dict['media'] >= 6:
            notas_dict['situacao'] = 'Boa'
        elif 6 > notas_dict['media'] >= 4:
            notas_dict['situacao'] = 'Ruim'
        else:
            notas_dict['situacao'] = 'Reprovado'
    return notas_dict


resp = notas(5, 3, 1, 6.5, 5,sit=True)
print(resp)
help(notas)