# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

y = int(input('Введите год: '))
leap = 0

if y % 400 == 0:
    leap = 1
elif y % 100 == 0:
    leap = 0
elif y % 4 == 0:
    leap = 1

print(
    f'Введенный год является {"високосным" if leap == 1 else "не високосным"}.')
