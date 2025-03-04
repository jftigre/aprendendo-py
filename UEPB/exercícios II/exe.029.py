'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um
colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo): aumento de 20%

salários entre R$ 280,00 e R$ 700,00: aumento de 15%

salários entre R$ 700,00 e R$ 1500,00: aumento de 10%

salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;

o percentual de aumento aplicado;

o valor do aumento;

o novo salário, após o aumento.
'''

salario = float(input('Digite o salário: '))

if salario < 0:
    print('salário inválido')
else:
    if salario <= 280:
        aumento_20 = salario * 1.2
        print(f'Após o aumento de 20% o salário de {salario} será de {aumento_20}')
    else:
        if  280 < salario <= 700:
            aumento_15 = salario * 1.15
            print(f'Após o aumento de 15% o salário de {salario} será de {aumento_15}')
        else:
            if 700 < salario <= 1500:
                aumento_10 = salario * 1.1
                print(f'Após o aumento de 10% o salário de {salario} será de {aumento_10}')
            else:
                if salario >= 1500:
                    aumento_5 = salario * 1.05
                    print(f'Após o aumento de 5% o salário de {salario} será de {aumento_5}')