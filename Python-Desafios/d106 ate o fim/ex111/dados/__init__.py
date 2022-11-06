def leiaDinheiro(entrada):
    entrada = input(entrada)

    while entrada.isnumeric() is False:

        if entrada.find('.') != -1 or entrada.find(',') != -1:

            if entrada.replace('.','',1).isnumeric():
                return float(entrada)
            elif entrada.replace(',','',1).isnumeric():
                return float(entrada.replace(',','.',1))


        print(f'\033[0;31m<ERRO> {entrada} é um preço inválido\33[m')
        entrada = input(f'Digite o preço: R$')   
    return int(entrada)
    