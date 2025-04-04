def maior(*num):
    num_maior = 0
    for n in range(len(num)):
        if n == 0:
            num_maior = num[n]
        elif num[n] > num_maior:
            num_maior = num[n]
    for i in num:
        print(i, end=' ')
    print(f'A lista possui {len(num)} números')
    print(f'O maior número é {num_maior}')


maior(2,3,5,7,9)
maior(10,100,4,5,99)
maior(3,5,70,90)
maior(1,800)
maior(189,1)
maior(0)
maior()