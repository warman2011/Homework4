from itertools import count, cycle
from time import time
st = input('Какие символы зациклить: ')
tm = int(input('Сколько по времени генерировать: '))
start = time()
for a in cycle(st):
    if time() > start+tm:
        break
    else:
        print(a)
