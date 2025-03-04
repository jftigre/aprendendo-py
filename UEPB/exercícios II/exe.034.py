'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir 
os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situaçõe
'''
import math


print('Data a fórmula ax2 + bx + c, determine os valores das variáveis para calcular as raízes.')

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - 4*a*c

if delta > 0:
    raiz_1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz_2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'As raízes da equação são {raiz_1:.2f} e {raiz_2:.2f}')
else:
    if delta == 0:
        raiz_1 = -b / (2 * a)
        print(f'A equação tem uma raiz real: {raiz_1:.2f}')
    else:
        print('A equação não tem raízes reais.')