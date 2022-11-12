from os import system
system('cls') or None

dict = {
        'vermelho' : '\033[0;31m',
        'limpar' : '\33[m'
}
def leiaint(textinput):

    while True:
        try:
            numero = int(input(textinput))

        except :
            print(dict['vermelho'],f'ERRO: por favor, digite um número inteiro válido.',dict['limpar'])

        else:
            return numero

def leiaReal(textinput):
    while True:
        try:
            numero = float(input(textinput))
        
        except (ValueError,TypeError):
            print(dict['vermelho'],'ERRO: por favor, digite um número real válido.',dict['limpar'])
        
        else:
            return numero

n1 = leiaint('Digite um Inteiro: ')
n2 = leiaReal('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2:.2f}')
