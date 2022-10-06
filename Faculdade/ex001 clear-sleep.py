from time import sleep
import os

for i in range(10):
    print(i)

sleep(3)
os.system('cls') or None

for i in range(10, 20):
    print(i)

sleep(3)
os.system('cls') or None

for i in range(10, 150, 27):
    print(i)
    if i % 2 == 0:
        print("par\n")
    else:
        print("impar\n")

sleep(4)
os.system('cls') or None

i = 1
while i % 2 != 0:
    i = int(input(f'Digite o valor de i: '))
else:
    print('Digitou par, e saiu do looping!')
