import datetime

maior = 0
menor = 0

for i in range(7):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = datetime.date.today().year - nascimento
    if idade >=18:
        maior += 1
    else:
        menor += 1

print('Maior:', maior)
print('Menor:', menor)