'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido.'''

num = int(input('Digite um número: '))

dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

# Verifica se o número está entre 1 e 7 para acessar o índice correto
if 1 <= num <= 7:
    print(dias[num - 1])# Como a lista começa no índice 0, subtraímos 1 de 'num' para alinhar com o índice correto.
                        # Ex: num = 1 => acessa índice 0 (Domingo), num = 2 => acessa índice 1 (Segunda), etc.
else:
    print('Valor inválido!')

'''if num == 1:
    print('Domingo')
else:
    if num == 2:
        print('Segunda')
    else:
        if num == 3:
            print('Terça')
        else:
            if num == 4:
                print('Quarta')
            else:
                if num == 5:
                    print('Quinta')
                else:
                    if num == 6:
                        print('Sexta')
                    else:
                        if num == 7:
                            print('Sábado')
                        else:
                            print('Valor inválido !')
                            '''