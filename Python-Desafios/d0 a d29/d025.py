'''
nome = input('Digite o seu nome: ')
if nome.lower().find('silva') != -1:
    print('Tem silva no nome SIM!!')
else:
    print("Não tem silva no nome")
'''
nome = input('Qual é o seu nome: ').strip()
print(f'Tem silva? {"silva" in nome.lower()}')
# assim ele procura silva em nome, e retorna true ou false
