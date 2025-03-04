'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total 
do seu salário no referido mês.'''

ganha = float(input('Quanto você ganha por hora ? '))
horas = float(input('Quantas horas você trabalha ? '))
salário = ganha * horas

print(f'O salário referente a esse mês é igual a {salário}')