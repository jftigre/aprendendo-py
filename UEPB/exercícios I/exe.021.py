'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
 Imposto de Renda, 8% para o INSS e 5% para osindicato, faça um programa que nos dê:
 a) salário bruto.
 b) quanto pagou ao INSS.
 c) quanto pagou ao sindicato.
 d) o salário líquido.
 e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
 Salário Bruto : R$IR (11%) : 
 R$INSS (8%) : 
 R$Sindicato ( 5%) : 
 R$Salário Liquido : 
 R$Obs.: Salário Bruto - Descontos = Salário Líquido.'''

hr = float(input('Digite seu ganho por hora: '))
jornada = int(input('Digite sua jornada de trabalho no mês: '))

salario_bruto = hr * jornada
ir = salario_bruto * 0.11  # 11% de Imposto de Renda
inss = salario_bruto * 0.08  # 8% de INSS
sindicato = salario_bruto * 0.05  # 5% para o sindicato
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"\nSalário Bruto : R$ {salario_bruto:.2f}")
print(f"(-) IR (11%) : R$ {ir:.2f}")
print(f"(-) INSS (8%) : R$ {inss:.2f}")
print(f"(-) Sindicato (5%) : R$ {sindicato:.2f}")
print(f"= Salário Líquido : R$ {salario_liquido:.2f}")
