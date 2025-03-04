'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário 
bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário 
o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento

Salário Bruto até 1500 (inclusive) - desconto de 5%

Salário Bruto até 2500 (inclusive) - desconto de 10%

Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

i. Salário Bruto: (5 * 220) : R$ 1100,00

ii. (-) IR (5%) : R$ 55,00

iii. (-) INSS ( 10%) : R$ 110,00

iv. FGTS (11%) : R$ 121,00

v. Total de descontos : R$ 165,00

vi. Salário Liquido : R$ 935,00
'''

valor_hora = float(input('Digite o valor da hora trabalhada: '))
tempo_trabalho = int(input('Digite a jornada de trabalho (em horas): '))

salario_bruto = valor_hora * tempo_trabalho

if salario_bruto <= 900:
    ir = 0
else:
    if salario_bruto <= 1500:
        ir = salario_bruto * 0.05
    else:
        if salario_bruto <= 2500:
            ir = salario_bruto * 0.10
        else:
            ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f'\nSalário Bruto: (R$ {valor_hora} * {tempo_trabalho}) : R$ {salario_bruto:.2f}')
print(f'(-) IR: R$ {ir:.2f}')
print(f'(-) INSS (10%): R$ {inss:.2f}')
print(f'(-) Sindicato (3%): R$ {sindicato:.2f}')
print(f'FGTS (11%) : R$ {fgts:.2f}')
print(f'Total de Descontos: R$ {total_descontos:.2f}')
print(f'Salário Líquido: R$ {salario_liquido:.2f}')

