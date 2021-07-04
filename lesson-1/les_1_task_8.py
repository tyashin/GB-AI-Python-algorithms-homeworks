# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
num_3 = float(input('Введите третье число: '))

max_num = max(num_1, num_2, num_3)
min_num = min(num_1, num_2, num_3)

if max_num > num_1 > min_num:
    print(f'{num_1} - среднее число.')
elif max_num > num_2 > min_num:
    print(f'{num_2} - среднее число.')
elif max_num > num_3 > min_num:
    print(f'{num_3} - среднее число.')
else:
    print('Среднее число не найдено.')


# или более простой вариант :))
print(f'Среднее число: {num_1 + num_2 + num_3 - max_num - min_num }')
