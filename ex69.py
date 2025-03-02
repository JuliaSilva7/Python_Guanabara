mulheres_jovens = homens = maiores = 0

print('CADASTRO DE PESSOAS')
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [F/M]: ').upper().strip()
    if sexo == 'F' and idade < 20:
        mulheres_jovens += 1

    if sexo == 'M':
        homens += 1

    if idade >= 18:
        maiores += 1

    continuar = ' '
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar? [S/N]').strip().upper()

    if continuar == 'N':
        break

print(f'Maiores de idade: {maiores}')
print(f'Mulheres com menos de 20: {mulheres_jovens}')
print(f'Pessoas do sexo masculino: {homens}')
