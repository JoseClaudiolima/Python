import os
os.system('cls') or None

a = 5
abcdario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while a != 0:
    TextoFinal = ""
    opcao = input(f'''1- Criptografar
2-Descriptografar
Sua escolha: ''')
    while opcao not in '12':
        opcao = str(input(f'''1- Criptografar
2-Descriptografar
Sua escolha: '''))
    opcao = int(opcao)
    texto = input(f'Digite o texto: ').upper()
    chave = input(f'Digite a chave: ').upper()
    while len(chave) > len(texto):
        print(f'Atenção, a chave não pode ser maior que o texto')
        chave = input(f'Escolha outra chave compativel: ').upper()
        print(len(chave), len(texto))
    chaveFinal = ''
    i = 0
    while len(chaveFinal) < len(texto):
        chaveFinal += chave[i]
        i += 1
        if (i == len(chave)):
            i = 0
    for i in range(len(texto)):
        if texto[i] != ' ':
            posição_letra_frase = int(abcdario.index(texto[i]))
            posição_letra_chave = int(abcdario.index(chaveFinal[i]))

            if opcao == 1:
                TextoFinal += abcdario[(posição_letra_frase + posição_letra_chave) % len(abcdario)]
            else:
                TextoFinal += abcdario[(posição_letra_frase - posição_letra_chave) % len(abcdario)]
        else:
            TextoFinal += ' '
    print(f'Frase final: {TextoFinal}')
    a = 0
