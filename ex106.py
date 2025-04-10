from time import sleep
c = ('\033[m','\033[30;107m', '\033[37;40m')

def help_python(comando):
    titulo(f'Acessando o manual do comando {comando}', 2)
    sleep(1)
    print(c[2])
    help(comando)
    print(c[0])

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end= '')
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)
    print(c[0], end='')

while True:
    titulo('Sistema de ajuda Pyhelp',1)
    ajuda = input('Digite a função ou biblioteca (Digite fim para sair ) > ')
    if ajuda.upper() == 'FIM':
        break
    else:
        help_python(ajuda)

titulo('Até logo',1)
