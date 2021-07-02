# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
num_3 = float(input('Введите третье число: '))

max_num = max(num_1, num_2, num_3)
min_num = min(num_1, num_2, num_3)

if num_1 > min_num and num_1 < max_num:
    print(f'{num_1} - среднее число.')
elif num_2 > min_num and num_2 < max_num:
    print(f'{num_2} - среднее число.')
elif num_3 > min_num and num_3 < max_num:
    print(f'{num_3} - среднее число.')
else:
    print('Среднее число не найдено.')
