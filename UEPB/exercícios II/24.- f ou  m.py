'''24. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

letra = input('Digite F ou M: ').upper().strip()

if letra == 'F':
    print('Você selecionou F - Feminino')
else:
    if letra == 'M':
        print('Você selecionou M - Masculino')
    else:
        print('Valor inválido!')
