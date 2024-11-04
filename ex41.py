import datetime

print('*' * 30)
print('     Categorias de Natação')
print('*' * 30)

nasc = int(input('Qual o ano de nascimento do atleta? '))
atual = datetime.date.today().year
idade = atual - nasc

if idade <= 9:
    print(f'Esse atleta tem {idade} anos. Ele pertence à categoria MIRIM')
elif 9 < idade <= 14:
    print(f'Esse atleta tem {idade} anos. Ele pertence à categoria INFANTIL')
elif 14 < idade <= 19:
    print(f'Esse atleta tem {idade} anos. Ele pertence à categoria JUNIOR')
elif 19 < idade <= 25:
    print(f'Esse atleta tem {idade} anos. Ele pertence à categoria SÊNIOR')
else:
    print(f'Esse atleta tem {idade} anos. Ele pertence à categoria MASTER')
