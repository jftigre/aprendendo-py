'''Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas 
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.'''


nome = str(input('Digite o nome do vendedor: '))
salario_fixo = float(input('Digite o salário fixo: '))
total_vendas = float(input('Digite o total, em reais, das suas vendas: '))
vendas_comissao = total_vendas * 0.15

print(f'''O vendedor(a), {nome}, tem o salário fixo de R${salario_fixo}.
Além disso, terá uma comissão de R${vendas_comissao}''')