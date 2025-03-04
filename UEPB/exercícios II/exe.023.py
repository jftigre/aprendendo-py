'''23. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

numero = float(input('Digite um número: '))

if numero == 0:
    print('0 é um número NULO.')

if numero > 0:
    print(f'{numero} é um número positivo.')

if numero < 0:
    print(f'{numero} é um número negativo.')
