import datetime

ano = int(input('Escreva um ano (escreva 0 para o ao atual): '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')
