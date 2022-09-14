import random
nome1 = input(f'Digite o integrante n°1 do grupo: ')
nome2 = input(f'Digite o integrante n°2 do grupo: ')
nome3 = input(f'Digite o integrante n°3 do grupo: ')
nome4 = input(f'Digite o integrante n°4 do grupo: ')
grupo = [nome1, nome2, nome3, nome4]

random.shuffle(grupo)
print(f'A ordem de apresentação será:')
print(grupo)
