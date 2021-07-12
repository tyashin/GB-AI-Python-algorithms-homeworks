'''
4. Определить, какое число в массиве встречается чаще всего.

Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.
Если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.

'''

from random import randint
LENGTH = 10

a = [randint(0, 5) for i in range(LENGTH)]
max_count = [0, 0]

for i in range(0, LENGTH-1):
    count = 1
    for j in range(i+1, LENGTH):
        if a[i] == a[j]:
            count += 1
    if count > max_count[1]:
        max_count[0] = i
        max_count[1] = count

print(f'Массив: {a}')
if max_count[1] > 1:
    print(
        f'Самый распространенный элемент: {a[max_count[0]]}. Он встречается {max_count[1]} раз(а).')
else:
    print('Каждый элемент массива встречается не более одного раза.')
