'''Escreva um programa que leia três números inteiros e positivos (1, 2, 3) 
e calcule aseguinte expressão:'''

'''
D = (R + S)/2
R = (1 + 2)**2 
S = (2 + 3)**2

'''

numeros = []

for i in range(1, 4):
    num = int(input(f'Digite o {i}ª número: '))
    numeros.append(num)

#PEGANDO DA LISTA
n1 = numeros[0]
n2 = numeros[1]
n3 = numeros[2]

r = (n1 + n2)**2
s = (n2 + n3)**2
d = (r + s)/2

print(f'O valor de D é igual a {d}')
