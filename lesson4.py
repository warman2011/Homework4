from random import randrange
other_list = []
new_list = [el * randrange(1, 3) for el in range(1, 30)]
print(new_list)
for x in new_list:
    if new_list.count(x) < 2:
        other_list.append(x)
print(other_list)
