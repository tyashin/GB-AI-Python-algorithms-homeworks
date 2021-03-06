'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. 
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

'''

from random import randint


def bubble_sort(array):
    sorted = True
    for i in range(SIZE):
        for j in range(0, SIZE-i-1):
            if array[j] < array[j+1]:
                sorted = False
                array[j], array[j+1] = array[j+1], array[j]

        if sorted == True:
            break

    return array


SIZE = 10
array = [randint(-100, 101) for i in range(SIZE)]
print(f'До сортировки: {array}')
print(f'После сортировки: {bubble_sort(array)}')
