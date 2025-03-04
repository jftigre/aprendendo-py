'''Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).'''

temperatura = float(input('Digite a temperatura (F): '))
C = (5 * (temperatura-32) / 9)

print(f'{temperatura}F equivale a {C:.2f}°C')