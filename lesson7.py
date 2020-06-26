from math import factorial
n = int(input('Введите число n: '))
def fact(n):
    for el in range(1, n):
        yield factorial(el)

for el in fact(n):
    print(el)

