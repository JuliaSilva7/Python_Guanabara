cadastro = []
registro = {}
media = soma = 0

while True:
    registro['nome'] = input('Nome: ')
    while True:
        registro['sexo'] = input('Sexo[M/F]: ').upper()
        if registro['sexo'] in 'MF':
            break
        print('Erro! Digite novamente. ')
    registro['idade'] = int(input('Idade: '))
    cadastro.append(registro.copy())
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = input('Deseja continuar? [S/N] : ').upper().strip()
    if continuar == 'N':
        break
print('-='*30)
print(f'O grupo tem {len(cadastro)} pessoas.')
for i in cadastro:
    soma += i['idade']
media = soma/len(cadastro)
print(f'A média de idade é de {media:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for j in cadastro:
    if j['sexo'] == 'F':
        print(f'{j["nome"]} ', end=' ')
print(f'\nLista das pessoas que estão com idade acima da média: ')
for k in cadastro:
    if k['idade'] > media:
        print(f'Nome: {k["nome"]}; Sexo: {k['sexo']}; Idade: {k["idade"]} ')
