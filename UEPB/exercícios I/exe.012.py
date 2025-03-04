'''A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. 
Faça um algoritmo que receba um valor de uma compra e mostre o valor dasprestações'''

valor = float(input('Digite o valor do produto: '))

prestacoes = valor / 5

print(f'Cada prestação custará R${prestacoes}')