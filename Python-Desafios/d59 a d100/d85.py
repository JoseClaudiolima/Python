from os import system
system('cls') or None

array = [[], []]

for i in range(7):
    entrada = input(f'Digite o  {i+1}° valor: ')
    while entrada.isnumeric() is False:
        entrada = input(f'Digite o {i+1}° valor: ')
    entrada = int(entrada)

    if entrada % 2 == 0:
        array[0].append(entrada)
    else:
        array[1].append(entrada)
array[0].sort()
array[1].sort()
print('-=' * 30)
print(
    f'''Os valores pares digitados foram: {array[0]}\nOs valores impares digitados foram: {array[1]}''')
