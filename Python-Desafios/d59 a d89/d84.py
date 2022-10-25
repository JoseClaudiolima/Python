from os import system
from random import randint
system('cls') or None
entrada = []
c = 1
pgordas = ''
pmagro = ''
while True:
    system('cls') or None
    entrada.append(input(f'Digite o seu nome: '))
    entrada.append(input(f'Digite o seu peso: '))
    #entrada.append(str(randint(50, 200)))
    while entrada[c].isnumeric() is False:
        entrada.insert(c, input(f'Digite o seu peso: (numerico) '))
    entrada[c] = int(entrada[c])
    if c == 1:
        maiorpeso = entrada[1]
        pgordas = entrada[0]
        menorpeso = entrada[1]
        pmagro = entrada[0]
    elif entrada[c] == maiorpeso:
        pgordas += '/'+str(entrada[c-1])
    elif entrada[c] > maiorpeso:
        maiorpeso = entrada[c]
        pgordas = entrada[c-1]

    if menorpeso == entrada[c] and c != 1:
        pmagro += '/'+str(entrada[c-1])
    if menorpeso > entrada[c]:
        menorpeso = entrada[c]
        pmagro = entrada[c-1]

    c += 2
    verific = input(f'Deseja continua? ')
    while verific not in 'SsNn':
        verific = input(f'Deseja continua? [S/N]')
    if verific in 'Nn':
        break
print('-='*30)
print(f'Foram cadastradas {len(entrada)/2} pessoas.')
print(f'O maior peso foi de {maiorpeso} de {pgordas}.')
print(f'O menor peso foi de {menorpeso} de {pmagro}.')
