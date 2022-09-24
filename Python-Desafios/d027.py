nome = input('Digite seu nome: ')
print(
    f'Seu primeiro nome: {nome.split()[0]}, seu ultimo nome: {nome.split()[len(nome.split())-1]}')
