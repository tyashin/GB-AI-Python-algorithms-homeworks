'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.

Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.

'''

import re
from collections import namedtuple
from statistics import mean
from sys import exit

Enterprise = namedtuple(
    'Enterprise', ['title', 'q1', 'q2', 'q3', 'q4', 'profit'])
regex = '^[-]?[0-9]*[,.]?[0-9]*$'
ent_num = int(input('Введите количество предприятий: '))
ent_list = []

for i in range(ent_num):
    ent_info = input(
        'Введите через пробел название предприятия и значения прибыли за каждый из 4-х кварталов: ').split()

    if len(ent_info) != 5 or len([i for i in ent_info if re.search(regex, i)]) != 4:
        print('Ошибка ввода.')
        exit()

    ent_list.append(Enterprise(*ent_info, sum(
        float(j) for j in ent_info[1:])))

avg_total = mean([i.profit for i in ent_list])
print(f'Средняя прибыль по всем предприятиям: {avg_total}.')

for i in ent_list:
    print(
        f'Предприятие: {i.title}. Прибыль за четыре квартала: {i.profit}.')

for i in ent_list:
    if i.profit > avg_total:
        print(f'Прибыль предприятия {i.title} выше средней.')
    elif i.profit < avg_total:
        print(f'Прибыль предприятия {i.title} ниже средней.')
