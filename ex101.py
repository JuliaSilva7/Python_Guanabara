from datetime import date


def voto(ano_nascimento):
    """ Função que determina o status de votação para uma pessoa de acordo com o seu ano de nascimento.
    Parâmetro: ano_nascimento (int)
    1 - Se for menor de 16, o voto é negado.
    2 - Se tiver entre 16 e menos de 18 é opcional. Com 65 ou mais também é opcional.
    3 - Se tiver entre 18 e 65 anos, é obrigatório votar"""
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


nascimento = int(input('Digite o ano de nascimento: '))
status = voto(nascimento)
print(status)
