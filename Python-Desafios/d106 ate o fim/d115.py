from ex115.interface import *
from ex115.arquivo import *
from os import system
from time import sleep
system('cls') or None


arq = 'bancodedados.txt'
verificoarquivo(arq)

while True:

    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta ==2 :
        cabeçalho('Opção 2')
    elif resposta ==3 :
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\33[m')
    sleep(2)