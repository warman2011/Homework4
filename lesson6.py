from itertools import count, cycle
from time import time
st = int(input('С какого числа начать генерацию: '))
tm = int(input('Сколько по времени генерировать: '))
start = time()
for a in count(st):
    if time() > start+tm:
        break
    else:
        print(a)
