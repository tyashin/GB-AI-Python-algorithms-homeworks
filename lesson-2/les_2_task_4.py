# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

'''
Пользователь вводит только натуральные числа.
Попытайтесь решить задания без использования массивов в любых вариациях(массивы будут рассмотрены на следующем уроке). 
Для простоты понимания любые квадратные скобки[и] считаются массивами и их наличие в коде расценивается как неверное решение.
'''

n = int(input('Введите количество элементов: '))
print(f'Сумма {n} элементов = {(1 - pow(-0.5, n))/1.5}')