'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, используйте метод сортировки, 
который не рассматривался на уроках (сортировка слиянием также недопустима).

'''

from random import randint


def find_median(arr, k):
    '''
    Использованная реализация Quickselect-алгоритма: 
    https://stackoverflow.com/a/25510441
    '''

    arr_len = len(arr)
    if arr_len == 1:
        return arr[0]

    pivot_ind = randint(0, arr_len-1)
    pivot = arr[pivot_ind]

    left_arr = [x for i, x in enumerate(
        arr) if x <= pivot and i != pivot_ind]
    right_arr = [x for i, x in enumerate(arr) if x > pivot and i != pivot_ind]

    m = len(left_arr)
    if k == m:
        return pivot
    elif k < m:
        return find_median(left_arr, k)
    else:
        return find_median(right_arr, k-m-1)


M = 5
array = [randint(0, 101) for i in range(2*M+1)]
print(f'Массив: {array}')
k = len(array) // 2
print(f'Медиана = {find_median(array, k)}')
