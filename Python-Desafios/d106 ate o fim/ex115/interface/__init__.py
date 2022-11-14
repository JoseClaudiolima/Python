def leiaint(textinput):
    while True:
        try:
            numero = int(input(textinput))
        except :
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return numero

def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\33[m')
        c +=1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \33[m')
    return opc
    