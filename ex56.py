soma_idade = 0
homem_mais_velho = 0
mulheres_jovens = 0
media = 0

for i in range(4):
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ').lower().strip()
    soma_idade += idade
    if sexo == 'm' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres_jovens += 1

media = soma_idade / 4
print(f'A média de idade é de {media:.2f}')
if homem_mais_velho == 0:
    print('Não existem homens na amostra')
else:
    print(f'A idade do homem mais velho é {homem_mais_velho} e seu nome é {nome_mais_velho}')
if mulheres_jovens == 0:
    print('Não existem mulheres com idade menor que 20')
else:
    print(f'Quantidade de mulheres com idade menor que 20 é de: {mulheres_jovens}')
