# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

'''
Пользователь вводит только натуральные числа.
Попытайтесь решить задания без использования массивов в любых вариациях(массивы будут рассмотрены на следующем уроке). 
Для простоты понимания любые квадратные скобки[и] считаются массивами и их наличие в коде расценивается как неверное решение.
'''

num = int(input('Введите натуральное число: '))
backwards = 0
while num > 0:
    backwards = backwards*10 + num % 10
    num = num//10

print(f'Обратное число: {backwards}')
