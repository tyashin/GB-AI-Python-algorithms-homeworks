'''
1. Определение количества различных подстрок с использованием хеш-функции. 
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() 
или любой другой из модуля hashlib задача считается не решённой.
'''

from hashlib import sha1
from itertools import combinations


def count_substrings(string: str) -> int:
    s_length = len(string)
    assert s_length, "Введена пустая строка!"
    string_hash = sha1(string.encode("utf-8")).hexdigest()
    substrings = [(string[x:y]) for x, y in combinations(
            range(len(string) + 1), r = 2)]

    result = []

    for i in substrings:
        used = False
        substring_hash = sha1(i.encode("utf-8")).hexdigest()

        if (substring_hash == string_hash and i == string) or (not i.strip()):
            continue

        for j in result:
            if substring_hash == sha1(j.encode("utf-8")).hexdigest() and i == j:
                used = True
                break

        if not used:
            result.append(i)

    print (f'Подстроки: {result}')
    return len(result)


s = input("Введите строку: ")
print(f'Количество подстрок: {count_substrings(s)}')



