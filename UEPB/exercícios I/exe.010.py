'''Elaborar um algoritmo que efetue a apresentação do valor da conversão em real 
(R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
dólar e também a quantidade de dólares disponíveis com o usuário.'''

cotacao_dolar = float(input('Digite a cotação do dólar: '))
quanto_dolar = float(input('Digite o valor em dólar: '))

conversor = quanto_dolar * cotacao_dolar

print(f'O valor final {conversor}')