import os
from time import sleep

os.system('cls') or None

for i in range(10, -1, -1):
    print(f'{i}', '.'*i)
    sleep(1)
print(f'BUUW POOOW')
