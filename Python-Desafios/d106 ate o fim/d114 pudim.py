from urllib import request
from os import system
system('cls') or None

try:
    site=request.urlopen('http://www.pudim.com.br/')
except request.URLError:
    print('O site do Pudim não está acessível no momento')
else:
    print('Consegui abrir site do pudim com sucesso!')