'''22. Faça um Programa que peça dois números e imprima o maior deles.'''

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))

if numero_1 > numero_2:
    print(f'O primeiro número, {numero_1}, é maior que o segundo, {numero_2}.')
else:
    print(f'O segundo número, {numero_2}, é maior que o primeiro, {numero_1}.')
    if numero_1 == numero_2:
        print('Os números são iguais!!!')