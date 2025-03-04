'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino 
ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso.'''

mensagem = '''Digite o turno que você estuda:
[M - Matutino, V - Vespertino, N - Noturno]'''
print(mensagem)

turno = input('Turno escolhido: ').strip().upper()

if turno == 'M':
    print('Bom dia !!!')
else:
    if turno == 'V':
        print('Boa tarde !!!')
    else:
        if turno == 'N':
            print('Boa noite !!!')
        else:
            print('Valor Inválido!')