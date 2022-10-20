from os import system
system('cls') or None

dados = []
entrada = []
while True:
    entrada.append(input(f'Digite o seu nome: '))
    entrada.append(input(f'Digite o seu peso: '))
    while entrada[1].isnumeric() is False:
        entrada.insert(1, input(f'Digite o seu peso: (numerico) '))
    break
