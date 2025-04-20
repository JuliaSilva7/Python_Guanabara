def linha(n=50):
    print('-' * n)


def cabecalho(msg):
    linha()
    print(f'{msg.center(50)}')
    linha()


def abrirarquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Falha ao criar o arquivo')
    else:
        print('Arquivo criado com sucesso')


def listar():
    with open("registro.txt", "r", encoding="utf-8") as arquivo:
        linha()
        linhas = arquivo.readlines()
        for i in range(0, len(linhas), 2):
            nome = linhas[i].strip()
            idade = linhas[i + 1].strip()
            print(f"{nome.ljust(10)} {idade.rjust(3)}")
        linha()


def registrar(nome='desconhecido',idade='0'):
    with open("registro.txt", "a", encoding="utf-8") as arquivo:
        try:
            while True:
                nome.strip()
                if nome.isalpha():
                    arquivo.write(f'{nome}\n')
                    break
                print('Digite um nome válido')
            while True:
                idade.strip()
                if idade.isnumeric():
                    arquivo.write(f'{idade}\n')
                    break
                print('Digite uma idade válida')
        except:
            print('Erro nos valores digitados. Digite novamente.')
