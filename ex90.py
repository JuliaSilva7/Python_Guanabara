aluno = dict()

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))

print(f'O nome do aluno é {aluno['nome']}')
print(f'A média é igual a {aluno['media']}')
if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['status'] = 'Recuperação'
else:
    aluno['status'] = 'Reprovado'
print(f'A situação do aluno é {aluno['status']}')
