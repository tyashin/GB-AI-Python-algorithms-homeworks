'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.

'''

from collections import defaultdict, deque


class Hex_arithmetic():

    def __init__(self, num1, num2):
        self.hex_digits = [str(i) for i in range(10)] + \
            ['A', 'B', 'C', 'D', 'E', 'F']

        self.num1 = num1.upper()
        self.num2 = num2.upper()

        if len(self.num1) < len(self.num2):
            self.num1, self.num2 = self.num2, self.num1

    def add_hex_nums(self, n1=None, n2=None):
        carry_on = 0
        sum = []

        if n1 == n2 == None:
            n1 = self.num1[:][::-1]
            n2 = self.num2[:][::-1]
        else:
            n1 = n1[::-1]
            n2 = n2[::-1]
            if len(n1) < len(n2):
                n1, n2 = n2, n1

        for i in range(len(n1)):
            digit = self.hex_digits.index(
                n1[i]) + (self.hex_digits.index(n2[i]) if i < len(n2) else 0) + carry_on

            if digit > 15:
                digit = digit - 16
                carry_on = 1
            else:
                carry_on = 0

            sum.append(self.hex_digits[digit])

        if carry_on == 1:
            sum.append(self.hex_digits[1])

        return sum[::-1]

    def multiply_hex_nums(self):
        carry_on = 0
        num_dict = defaultdict(int)
        k = 0
        n1 = self.num1[:][::-1]
        n2 = self.num2[:][::-1]

        for i in range(len(n2)):
            num_list = deque()

            for _ in range(i):
                num_list.appendleft("0")

            for j in range(len(n1)):

                digit = self.hex_digits.index(n1[j]) * \
                    self.hex_digits.index(n2[i]) + carry_on

                if digit > 15:
                    spam = digit % 16
                    carry_on = (digit - spam)//16
                    digit = spam

                else:
                    carry_on = 0

                num_list.append(self.hex_digits[digit])

            while carry_on > 0:
                if carry_on > 15:
                    digit = carry_on % 16
                    carry_on = carry_on - 16
                    num_list.append(self.hex_digits[digit])
                else:
                    num_list.append(self.hex_digits[carry_on])
                    carry_on = 0

            num_dict[k] = num_list
            k += 1

        product = ['0']
        for i in num_dict.values():
            product = self.add_hex_nums(product, list(i)[::-1])

        return product


num1 = input('Введите первое шестнадцатеричное число:')
num2 = input('Введите второе шестнадцатеричное число:')
ha = Hex_arithmetic(num1, num2)
print(f'{ha.num1} + {ha.num2} = {ha.add_hex_nums()}')
print(f'{ha.num1} * {ha.num2} = {ha.multiply_hex_nums()}')
