import datetime
registro = dict()

registro['nome'] = input('Digite o nome: ')
nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento
registro['idade'] = idade
registro['ctps'] = int(input('Digite sua CTPS (0 não tem): '))
if registro['ctps'] != 0:
    registro['contratacao'] = int(input('Digite o ano da contratação: '))
    registro['salario'] = float(input('Digite o seu salário: '))
    contribuicao = 35 - (ano_atual - registro['contratacao'])
    registro['aposentadoria'] = idade + contribuicao

for k,l in registro.items():
    print(f'{k} tem o valor {l}')
