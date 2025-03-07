clubes_serie_a = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthians','Bahia','Cruzeiro','Vasco','Vitória','Atlético MG','Fluminense','Grêmio','Juventude','Bragantino','Athletico PR','Criciúma','Cuiabá','Atlético Goianiense')

print(f'Os clubes da série A: {clubes_serie_a}')
print(f'Os 5 primeiros colocados da série A foram: {clubes_serie_a[:5]}')
print(f'Os 4 últimos são: {clubes_serie_a[-4:]}')
print(f'Times em ordem alfabetica {sorted(clubes_serie_a)}')

for posicao , clube in enumerate(clubes_serie_a, start=1):
    if clube == 'Bahia':
        print(f'O {clube} está na {posicao}ª posição.')