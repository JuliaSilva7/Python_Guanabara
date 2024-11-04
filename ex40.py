n1 = float(input('Escreva a nota: '))
n2 = float(input('Escreva a 2ª nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média é {media:.2f}. Você foi reprovado')
elif 7 > media >= 5:
    print(f'Sua média é de {media:.2f}. Você deve entrar na recuperação')
else:
    print(f'Você foi aprovado. Sua média foi {media:.2f}')
