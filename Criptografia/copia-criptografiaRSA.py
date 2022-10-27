import random
from os import system
system('cls') or None


#Essa função retorna o mdc entre dois valores, usando o algoritmo de Euclides

#Porém antes de calcular o algoritmo de Euclides, é feito uma comparação entre os valores entrados para saber qual é o maior valor, coloquei a comparação caso no futuro queira colocar números aleatórios ae. mas acho que não vamos usar. 
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
    


# A função gera um número aleatório que seja acima de 1 e menor que o conjunto 'n' (que é o tamanho de conjunto das nossas chaves privadas), além disso o número precisa ser co-primo de 'n', por isso é feito um looping para que o numero tenha mdc entre ele e n igual a 1.

# Anotação: Números co-primos são aqueles números, que entre ELES não há divisor comum além de 1 (mdc entre eles é 1).

def chave_publica(n):
    while True:
        e = random.randrange(2,n)
        if mdc(n,e) == 1 and e !=145:
            return e
#se e for '145' a msg cifragem é igual a msg decifrada, e se for '127' mesmo a chave privada sendo igual a chave publica, isso não acontece. isso se n for 323 (p=17 q=19)



#Pesquisar depois sobre Inverso multiplicativo, inverso multiplicativo é o número mutiplicado para o resultado ser 1. ou seja, 10 . y = 1 --> y = 0,1......5 . y = 1 --> y = 0,5

#Achei complexo e não entendi, ele usou algoritmo de euclides estendidio para calcular o inverso multiplicativo de 'e' em uma equação estranha.
#link :lambda3.com.br/2013/01/entendendo-de-verdade-a-criptografia-rsa-parte-iii/
def chave_privada(totiente, e):
    d = 0
    while ((d* e) % totiente != 1):
        d+=1
    return d


#A cifragem em RSA, é feita letra a letra pela seguinte equação: lcifra = l ** chavepub % n

#Para realizar a cifragem, temos que ter definido a mensagem, chave publica (que é a de ciptografia) e o conjunto n.
# Tendo isso podemos aplicar a formula acima, porém a lógica por de trás dessa função é: transformamos letra a letra por vez em um número, e após isso combinamos (com exponenciação) com a chave publica, com isso o numero da letra cifrada aumentará muito podendo até passar do conjunto n estabelecido, para resolver esse problema, é necessário pegar o resto da divisão da letra cifrada com o conjunto, por fim temos a letra cifrada dentro do conjunto estabelecido.
def cifrar(mensagem,e,n):
    msg_cifrada = ''
    for letra in mensagem:
        k = (ord(letra) ** e) % n
        msg_cifrada += chr(k)
    return msg_cifrada


#Para decifrar é feito a mesma logíca, e equacação da cifragem, entretanto usamos a chave privada em vez da chave publica
def decifrar(mensagem,n,d):
    msg_decifrada = ''
    for letra in mensagem:
        k = (ord(letra) ** d) % n
        msg_decifrada += chr(k)
    return msg_decifrada



def rsa ():
    msg = 'Deu bom, confia'

    #Escolheu a chave privada, quando escolheu esses numeros primos
    p = 19 #211
    q = 17 #191
    n = p * q #323   

    #Este n é o tamanho do nosso conjunto. No site diz que "É necessário termos um conjunto finito de valores para que possamos fazer o caminho inverso ao realizado para cifrar nossa mensagem". Podemos, chamar nosso conjunto de 323.


    # Daqui para frente é a função totiente, totiente de n (323)
    #youtube.com/watch?v=3MryVNzS3o4&ab_channel=KhanAcademyBrasil explica totiente de forma facil
    # Totiente significa: a quantidade de co-primos de um numero que são menores que ele mesmo.
    # O totiente de dois numeros primos são os dois números escolhidos menos 1 cada, seguido de multiplicação 
    #Φ(x) = (p - 1) * (q - 1)
    
    totiente = (p - 1) * (q - 1)

    #Ao chamar a função de chave publica com o parâmetro de totiente, estamos pedindo que gere um número co-primo aleatório.
    e = chave_publica(totiente)

    print(f'Chave publica: ({e},{n})')
    #
    d = chave_privada(totiente,e)
    print(f'Chave privada: ({d},{n})')

    msg = cifrar(msg,e,n)
    print(f'Mensagem Cifrada: {msg}')

    msg = decifrar(msg,n,d)
    print(f'Mensagem Decifrada: {msg}')

rsa()
