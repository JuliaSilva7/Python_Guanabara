n = int(input('Digite um número inteiro: '))
primo = 0

for i in range(1, n + 1):
    resto = n % i
    if resto == 0:
        primo += 1

if primo == 2 :
    print('Esse número é primo')
else:
    print('Esse número não é primo')
