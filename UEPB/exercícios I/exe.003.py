'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

soma = 0

for i in range(1, 5):
    nota = float(input(f'Digite a nota da {i}ª prova: '))
    soma = soma + nota

media = soma / 4

print(f'A média final foi igual a: {media}')