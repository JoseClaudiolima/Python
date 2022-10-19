from os import system
system('cls') or None

array = []

for i in range(5):
    number = input(f'Digite um número:')
    while number.isnumeric() is False or int(number) in array:
        number = input(f'Número inválido, ou já digitado, tente novamente: ')

    if i == 0:
        print(f'Adicionado ao final da lista')
        array.append(int(number))
    else:
        for j in range(len(array)):
            if int(number) <= array[j]:
                array.insert(j, int(number))
                print(f'Adicionado na posição {j} da lista...')
                break
            elif int(number) > array[len(array)-1]:
                array.append(int(number))
                print(f'Adicionado ao final da lista...')
                break
print('-='*20)
print(array)
