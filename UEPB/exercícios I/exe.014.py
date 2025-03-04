'''Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida 
a distância total percorrida pelo automóvel e o total de combustível gasto.'''

distancia = float(input('Digite a distância pecorrida [km]: '))
combustivel = float(input('Digite quanto de combustível foi utilizado [l]: '))

consumo = distancia / combustivel

print(f'A autonomia do veículo foi de {consumo}km/l')
