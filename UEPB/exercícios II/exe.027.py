'''27. Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

produ_1 = float(input('Digite o valor do primeiro produto: '))
produ_2 = float(input('Digite o valor do segundo produto: '))
produ_3 = float(input('Digite o valor do terceiro produto: '))

if produ_1 <= produ_2 and produ_1 <= produ_3:
    print(f'O produto mais barato custa {produ_1}')
else:
    if produ_2 <= produ_1 and produ_2 <= produ_3:
        print(f'O produto mais barato custa {produ_2}')
    else:
        print(f'O produto mais barato custa {produ_3}')