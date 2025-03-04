'''Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
• o produto do dobro do primeiro com metade do segundo .
• a soma do triplo do primeiro com o terceiro.
• o terceiro elevado ao cubo'''

# Solicita os números ao usuário
int_1 = int(input('Digite o primeiro inteiro: '))
int_2 = int(input('Digite o segundo inteiro: '))
real = float(input('Digite o número real: '))

# Cálculos
exe01 = (2 * int_1) * (0.5 * int_2)  # Produto do dobro do primeiro com metade do segundo
exe02 = (3 * int_1) + real           # Soma do triplo do primeiro com o terceiro
exe03 = real ** 3                    # Terceiro número elevado ao cubo

# Exibição dos resultados
print(f'O primeiro exercício é igual a {exe01:.2f}')
print(f'O segundo exercício é igual a {exe02:.2f}')
print(f'O terceiro exercício é igual a {exe03:.2f}')
