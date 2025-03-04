'''Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento 
após um mês. Considere fixo o juro da poupança em 0,70% a. m'''

valor = float(input('Digite o valor que queria depositar: '))
juros = float(input('Digite o juros : '))
tempo = int(input('Digite quanto tempo renderá: '))

m = valor * (1 + (juros/100))**tempo

print(f'R${valor} após {tempo} meses renderá R${m:.2f}')