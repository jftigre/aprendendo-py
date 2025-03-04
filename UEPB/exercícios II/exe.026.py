'''Faça um Programa que leia três números e mostre o maior deles'''

num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))
num_3 = float(input('Digite o terceiro número: '))

if num_1 >= num_2 and num_1 >= num_3:
    print(f'O maior número é: {num_1}')
else:
    if num_2 >= num_1 and num_2 >= num_3:
        print(f'O maior número é: {num_2}')
    else:
        print(f'O maior número é: {num_3}')
