'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.

'''

from random import uniform


def merge_sort(arr):

    if len(arr) < 2:
        return arr

    result, mid_el = [], len(arr) // 2

    left = merge_sort(arr[:mid_el])
    right = merge_sort(arr[mid_el:])
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


SIZE = 10
array = [uniform(0, 50) for i in range(SIZE)]
print(f'До сортировки: {array}')
print(f'После сортировки: {merge_sort(array)}')
