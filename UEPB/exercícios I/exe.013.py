''' Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda.
Sabe-se que o preço de custo receberá um acréscimo de acordo com
um percentual informado pelo usuário.'''

preco_custo = float(input('Digite o preço de custo do produto: R$')) 
percentual = float(input('Digite o percentual de aumento: '))

preco_venda = preco_custo * (1 + (percentual/100))

print(f'O preço de venda será de R${preco_venda}')
