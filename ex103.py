def ficha(nome = "Desconhecido", gols = 0):
    if nome.strip() == "":
        nome = "Desconhecido"
    if gols == "":
        gols = 0
    return print(f'O jogador {nome} fez {gols} gols no campeonato.')


ficha('José')
ficha('Ricardo',78)
ficha(gols=50)
ficha()
