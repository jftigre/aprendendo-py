'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; Triângulo Equilátero: 
três lados iguais; Triângulo isósceles: quaisquer dois lados iguais; Triângulo Escaleno: três lados diferentes

'''
lado_1 = float(input('Digite o primeiro lado: '))
lado_2 = float(input('Digite o segundo lado: '))
lado_3 = float(input('Digite o terceiro lado: '))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    if lado_1 == lado_2 == lado_3:
        tipo = 'Equilátero'
    else:
        if lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
            tipo = 'Isósceles'
        else:
            tipo = 'Escaleno'
    
    print(f'Os lados formam um triângulo {tipo}.')
else:
    print('Os lados não formam um triângulo.')