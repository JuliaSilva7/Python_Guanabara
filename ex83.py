expressao = input('Digite sua expressao: ')
lista = []
for i in expressao:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(i)
            break

if len(lista) == 0:
    print(f'A expressão {expressao} está correta')
else:
    print(f'A expressão {expressao} está incorreta')
