from random import randrange
result = []
my_list = [el*randrange(1, 10) for el in range(1, 10)]
print(my_list)
for i in range(1, 9):
    if my_list[i-1] < my_list[i]:
        result.append(my_list[i])
print(result)
