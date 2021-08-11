'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''
from collections import Counter

def Huffman_encode(string: str) -> str:
    sorted_freqs = [(k,v) for k,v in sorted(Counter(string).items(), key=lambda item: item[1])]

    print(sorted_freqs)



s = input('Введите произвольную строку: ')
s_encoded = Huffman_encode(s)
print(f'Закодированная по Хаффману строка: {s_encoded}')