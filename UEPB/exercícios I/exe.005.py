'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
import math

raio = float(input('Digite a medida do raio(metros): '))

area = math.pi * (raio **2)

print(f"A área desse cículo é igual a {area:.2f} metros")