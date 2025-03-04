'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e
a velocidade de um link de Internet (em MBps), calcule e informe o tempo aproximado
de download do arquivo usando este link (em minutos).'''

arquivo = float(input('Qual o tamanho do arquivo ? '))
velocidade = float(input('Qual a velocidade da Internet ? '))

tempo = arquivo/(velocidade*60)

print(f'O tempo, aproximado, para o download é de {tempo} minutos')