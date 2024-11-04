import datetime

nasc = int(input('Qual ano você nasceu? '))

data = datetime.date.today().year

alistamento = nasc + 18

if data > alistamento:
    tempo = data - alistamento
    print(f'Seu tempo de alistamento já passou. Você está atrasado em {tempo} ano(s).')
elif data == alistamento:
    print('Você deve se alistar esse ano.')
else:
    tempo = alistamento - data
    print(f'Seu tempo de alistamento ainda não chegou. Faltam {tempo} ano(s).')
