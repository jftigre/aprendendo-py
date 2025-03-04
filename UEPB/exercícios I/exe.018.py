'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule 
seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58'''

peso = float(input('Qual o peso ? (Kg): '))
altura = float(input('Qual a altura ? (m) '))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'O IMC é {imc:.2f} e indica que está ABAIXO DO PESO IDEAL')
else:
    if 18.5 <= imc < 25:
        print(f'O IMC é {imc:.2f} e indica que está no PESO IDEAL')
    else:
        if 25 <= imc < 30:
            print(f'O IMC é {imc:.2f} e indica que está com SOBREPESO')
        else:
            if 30 <= imc < 40:
                print(f'O IMC é {imc:.2f} e indica que está com OBESIDADE')
            else:
                if imc > 40:
                    print(f'O IMC é {imc:.2f} e indica que está com OBESIDADE MÓRBIDA')