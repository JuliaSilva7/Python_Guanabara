import requests

try:
    site = requests.get('https://www.pudim.com.br')
    if site.status_code == 200:
        print('Conectado com sucesso!')
except:
    print('O site não está funcionando no momento')