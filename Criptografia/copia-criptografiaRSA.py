import random
from os import system
system('cls') or None


#Essa função retorna o mdc entre dois valores, usando o algoritmo de Euclides

#Porém antes de calcular o algoritmo de Euclides, é feito uma comparação entre os valores entrados para saber qual é o maior valor.
def mdc(a,b): 
    if a >b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    menorcopia = menor

    while menor !=0:
        menor = maior % menor
        maior = menorcopia
        menorcopia = menor  
    return maior
    

# A função da chave pública gera um número aleatório e enquanto o mdc entre o número aleatório e o parâmetro não for igual a 1, ele continua gerando outro número aleatório. E no final retorna aquele que o mdc é igual a 1

# É necessário colocar a verificação de mdc igual a 1 , pois desta forma garante que o número aleatório gerado será número primo. 
# Lembrando que Números primos são aqueles divisíveis apenas por 1 e por eles mesmos.
def chave_publica(n): 
    while True:
        e = random.randrange(2,n)
        if mdc(n,e) == 1:
            return e




#Pesquisar depois sobre Inverso multiplicativo
def chave_privada(totiente, e):
    d = 0
    while ((d* e) % totiente != 1):
        d+=1
    return d


#Pesquisar depois
def cifrar(mensagem,e,n):
    msg_cifrada = ''
    for letra in mensagem:
        k = (ord(letra) ** e) % n
        msg_cifrada += chr(k)
    return msg_cifrada

#Pesquisar depois
def decifrar(mensagem,n,d):
    msg_decifrada = ''
    for letra in mensagem:
        k = (ord(letra) ** d) % n
        msg_decifrada += chr(k)
    return msg_decifrada



def rsa ():
    msg = 'Exemplo qualquer'

    #Escolheu dois números primos, podemos fazer outra função que gere aleatóriamente um número primo, esses dois números são a base da nossa criptografia.
    p = 17
    q = 19
    n = p * q #697   

    #Este n é o tamanho do nosso conjunto. É necessário termos um conjunto finito de valores para que possamos fazer o caminho inverso ao realizado para cifrar nossa mensagem. Podemos, chamar nosso conjunto de 697.


    # Daqui para frente é a função totiente, totiente de n (697)
    # Totiente significa: a quantidade de co-primos de um numero que são menores que ele mesmo.
    # O totiente são os dois números primos escolhidos menos 1 cada, seguido de multiplicação 
    #(x) = (p - 1) * (q - 1)
    
    totiente = (p - 1) * (q - 1)

    e = chave_publica(totiente)

