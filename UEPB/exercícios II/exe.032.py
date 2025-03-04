'''
32. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento Conceito

Entre 9.0 e 10.0 A

Entre 7.5 e 9.0 B

Entre 6.0 e 7.5 C

Entre 4.0 e 6.0 D

Entre 4.0 e zero E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C 
ou “REPROVADO” se o conceito for D ou E.
'''

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2
if media < 0 or media > 10:
    print('Valor inválido')
else:
    if media >= 9:
        conceito = 'A'
        status = 'APROVADO'
    else:
        if media >= 7.5:
            conceito = 'B'
            status = 'APROVADO'
        else:
            if media >= 6:
                conceito = 'C'
                status = 'APROVADO'
            else:
                if media >= 4:
                    conceito = 'D'
                    status = 'REPROVADO'
                else:
                    conceito = 'E'
                    status = 'REPROVADO'

    print(f'A média foi igual a {media:.1f} e conceito {conceito}')
    print(status)
'''if media < 0:
    print('Valor inválido')
else:
    if 9 <= media <= 10:
        print(f'Aprovado, a média foi igual a {media} e conceito A')
    else:
        if 7.5 <= media < 9:
            print(f'Aprovado, a média foi igual a {media} e conceito B')
        else:
            if 6 <= media < 7.5:
                print(f'Aprovado, a média foi igual a {media} e conceito C')
            else:
                if 4 <= media < 6:
                    print(f'Reprovado, a média foi igual a {media} e conceito D')
                else:
                    if 0 <= media < 4:
                        print(f'Reprovado, a média foi igual a {media} e conceito E')'''